import command_line_utilities
import subprocess
import socket
import constants

from scapy.all import *
from datetime import datetime


def is_browser_open():
    browsers = ['Firefox', 'Chrome', 'Safari', 'Opera']
    for browser in browsers:
        process = subprocess.Popen('ps -ax | grep ' + browser, stdout=subprocess.PIPE, shell=True)
        process_output = command_line_utilities.convert_output_to_string(process)
        for output in process_output:
            if 'app/Contents/MacOS'.lower() in output.lower():
                return True

    return False


def is_previous_packet_too_close_in_time_to_current_packet(current_packet_arrival_time, packet_arrival_times,
                                                           packet_arrival_times_index):

    return False


def scan_user_internet_traffic():
    sniffed_data = sniff(filter="tcp port 80 and host " + socket.gethostbyname(socket.gethostname()),
                         timeout=30, count=0)
    keywords = ['GET', 'Host', 'Referer']
    keywords_found_times = {}
    output = []
    is_first_packet = True

    for packet in sniffed_data:
        packet_arrival_time = datetime.fromtimestamp(packet.time)
        objectionable_word_found = False

        if not is_first_packet:
            if is_previous_packet_too_close_in_time_to_current_packet(packet_arrival_time, packet_arrival_times,
                                                                      packet_arrival_times_index):
                break

        for keyword in keywords:
            if keyword in str(packet):
                for objectionable_word in constants.objectionable_words_list:
                    if objectionable_word in str(packet):
                        output.append('The keyword ' + objectionable_word + ' was found at ' + str(packet_arrival_time))
                        objectionable_word_found = True
                        break

            if objectionable_word_found:
                break

        if is_first_packet:
            is_first_packet = False

    if not output:
        first_packet_time = str(datetime.fromtimestamp(sniffed_data[0].time))
        last_packet_time = str(datetime.fromtimestamp(sniffed_data[len(sniffed_data) - 1].time))
        output.append('No questionable words were found during ' + first_packet_time + last_packet_time + '.')

    return output
