import netifaces as ni
import subprocess
import socket
import pcapy

from datetime import datetime, timedelta
from utilities import packet_utilities
from impacket.ImpactDecoder import *
from constants import constants
from database import queries


# a map that contains a packet and the
# packets recorded arrival time in
# which it was sniffed
sniffed_data = {}


def is_browser_open():
    """
    Checks the OS's current processes to determine
    if a browser is currently being run.

    :return:
    """
    browsers = ['Firefox', 'Chrome', 'Safari', 'Opera',
                'Maxthon', 'OmniWeb', 'Torch', 'Brave']
    for browser in browsers:
        process = subprocess.check_output('ps -ax | grep ' + browser, shell=True).split('\n')
        for output in process:
            if 'app/Contents/MacOS'.lower() in output.lower():
                return True

    return False


def get_current_network_interface():
    """
    Gets the current interface in which
    the network connection is passing through
    (e.g., it determines if network traffic
    is going through ethernet or wifi).

    :return:
    """
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


def format_packet(unformatted_packet, keyword):
    """
    Formats a packet by removing any unnecessary
    data that's not associated with the keyword.
    It will first remove all hex values from the
    packet, and then strips data that doesn't
    pertain to the passed in keyword parameter.

    :param unformatted_packet: the untouched packet
    :param keyword: a string that determines what
    data to keep when the packet is formatted
    (e.g., GET, HOST, REFERER)
    :return: a string that can be used to more
    easily parse useful and relevant packet data
    """
    no_hex_packet = packet_utilities.remove_hex_values_from_packet(unformatted_packet)
    formatted_packet = packet_utilities.parse_packet_data_by_keyword(no_hex_packet, keyword)

    return formatted_packet


def create_packet_map(packet_arrival_time, packet):
    """
    Creates a map that contains the packet's
    recorded arrival time in which the packet
    was sniffed, and also the packet itself.


    :param packet_arrival_time: an object that
    contains the date of the packets recorded
    arrival time
    :param packet: the packet itself
    :return: a map that contains formatted
    versions of the packet and the date of the packet
    """
    packet_map = {}

    for keyword in constants.packet_keywords:
        packet_map[keyword] = format_packet(packet, keyword)

    # format the time in a more recognizable format
    packet_arrival_time = datetime.strftime(packet_arrival_time, '%m-%d-%Y %H:%M:%S')
    packet_map[packet_arrival_time] = get_host_referer_values

    return packet_map


def insert_packets_into_database(obj_packets_data):
    """
    Calls the query that inserts each packet into
    the database.

    :param obj_packets_data: a list that contains
    maps of packet data
    :return:
    """
    queries.insert_packets(obj_packets_data)


def is_packet_from_whitelisted_website(packet):
    """
    Checks to see if a packet originated from
    a whitelisted website.

    :param packet:
    :return: True if the packet came from a
    whitelisted website; False if not
    """
    for site in constants.whitelisted_websites:
        if site in str(packet):
            return True

    return False


def store_packets(pkt_header, data):
    """
    Called when the packet sniffer is active,
    this method takes the data gathered over
    the network and stores it in a map.

    :param pkt_header: the header of the packet;
    this will contain the arrival time of the
    packet itself
    :param data: the packet before it has been
    decoded
    :return: a map with the key as the timestamp
    of the packet and the value as the packet
    itself
    """
    packet = EthDecoder().decode(data)
    packet_arrival_time = pkt_header.getts()
    sniffed_data[packet_arrival_time] = packet


def scan_user_internet_traffic(thread_queue):
    """
    Scans the network traffic of the user
    and saves any objectionable content
    into the database.

    :param thread_queue:
    :return:
    """
    objectionable_packets = []

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
                        objectionable_word_found = True
                        objectionable_packets.append(create_packet_map(arrival_time, str(packet)))
                        break

            if obj_word_found:
                break

    if objectionable_packets:
        insert_packets_into_database(objectionable_packets)
