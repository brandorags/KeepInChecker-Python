import netifaces as ni
import subprocess
import socket
import pcapy

from datetime import datetime, timedelta
from utilities import packet_utilities
from impacket.ImpactDecoder import *
from constants import constants
from database import queries


sniffed_data = {}


def is_browser_open():
    browsers = ['Firefox', 'Chrome', 'Safari', 'Opera',
                'Maxthon', 'OmniWeb', 'Torch', 'Brave']
    for browser in browsers:
        process = subprocess.check_output('ps -ax | grep ' + browser, shell=True).split('\n')
        for output in process:
            if 'app/Contents/MacOS'.lower() in output.lower():
                return True

    return False


def get_current_network_interface():
    current_network_interface = None
    comp_ip = socket.gethostbyname(socket.gethostname())
    interfaces = ni.interfaces()

    for interface in interfaces:
        try:
            interface_ip = ni.ifaddresses(interface)[ni.AF_INET][0]['addr']
            if str(interface_ip) == str(comp_ip):
                current_network_interface = interface
                break
        except:
            continue

    return current_network_interface


def save_packet(packet_arrival_time, packet):
    packet_map = {}
    packet_text_only = packet_utilities.remove_hex_values_from_packet(packet)

    for keyword in constants.packet_keywords:
        packet_map[keyword] = packet_utilities.parse_packet_data_by_keyword(packet_text_only, keyword)

    packet_map['Time'] = datetime.strftime(packet_arrival_time, '%d-%m-%Y %H:%M:%S')

    return packet_map


def insert_packets_into_database(obj_packets_data):
    queries.insert_packets(obj_packets_data)


def is_packet_from_whitelisted_website(packet):
    for site in constants.whitelisted_websites:
        if site in str(packet):
            return True

    return False


def is_previous_packet_too_close_in_time_to_current_packet(obj_word,
                                                           current_obj_word_packet_arrival_time,
                                                           obj_word_found_datetime):
    previous_obj_word_packet_arrival_time = obj_word_found_datetime[obj_word]
    time_difference = current_obj_word_packet_arrival_time - previous_obj_word_packet_arrival_time

    if timedelta.total_seconds(time_difference) < 5:
        return True

    return False


def store_packets(pkt_header, data):
    packet = EthDecoder().decode(data)
    packet_arrival_time = pkt_header.getts()
    sniffed_data[packet_arrival_time] = packet


def scan_user_internet_traffic(thread_queue):
    obj_packets_data = []
    obj_word_found_datetime = {}
    output = []

    interface = get_current_network_interface()
    max_bytes = 1024
    promiscuous_mode = False
    read_timeout = 100
    packet_sniffer = pcapy.open_live(interface, max_bytes, promiscuous_mode, read_timeout)

    number_of_packets_to_capture = 1000
    packet_sniffer.loop(number_of_packets_to_capture, store_packets)

    for packet_arrival_time, packet in sniffed_data.iteritems():
        if is_packet_from_whitelisted_website(packet):
            continue

        arrival_time = datetime.fromtimestamp(packet_arrival_time[0])
        obj_word_found = False

        for keyword in constants.packet_keywords:
            if keyword in str(packet):
                for obj_word in constants.objectionable_words_list:
                    if obj_word.lower() in str(packet).lower():
                        if obj_word in obj_word_found_datetime and \
                                is_previous_packet_too_close_in_time_to_current_packet(obj_word,
                                                                                       arrival_time,
                                                                                       obj_word_found_datetime):
                            break

                        obj_word_found = True
                        obj_word_found_datetime[obj_word] = arrival_time
                        output.append('The word ' + obj_word + ' was found at ' + str(arrival_time))

                        obj_packets_data.append(save_packet(arrival_time, str(packet)))
                        break

            if obj_word_found:
                break

    if obj_packets_data:
        insert_packets_into_database(obj_packets_data)

    thread_queue.put(output)
    return output
