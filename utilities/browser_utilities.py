import subprocess
import pcapy

from utilities import command_line_utilities, packet_utilities
from datetime import datetime, timedelta
from impacket.ImpactDecoder import *
from constants import constants
from database import queries


sniffed_data = {}


def is_browser_open():
    browsers = ['Firefox', 'Chrome', 'Safari', 'Opera']
    for browser in browsers:
        process = subprocess.Popen('ps -ax | grep ' + browser, stdout=subprocess.PIPE, shell=True)
        process_output = command_line_utilities.convert_output_to_string(process)
        for output in process_output:
            if 'app/Contents/MacOS'.lower() in output.lower():
                return True

    return False


def parse_packet(packet_arrival_time, packet):
    packet_map = {}

    for keyword in constants.packet_keywords:
        if keyword == 'GET':
            packet_map[keyword] = packet_utilities.parse_get_data(keyword, packet)
        elif keyword == 'Host':
            packet_map[keyword] = packet_utilities.parse_host_data(keyword, packet)
        else:
            packet_map[keyword] = packet_utilities.parse_referer_data(keyword, packet)

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

    max_bytes = 1024
    promiscuous_mode = False
    read_timeout = 100
    packet_sniffer = pcapy.open_live('en1', max_bytes, promiscuous_mode, read_timeout)

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

                        obj_packets_data.append(parse_packet(arrival_time, str(packet)))
                        break

            if obj_word_found:
                break

    if obj_packets_data:
        insert_packets_into_database(obj_packets_data)

    thread_queue.put(output)
    return output
