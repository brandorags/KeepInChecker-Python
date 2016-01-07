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


def scan_user_internet_traffic():
    sniffed_data = sniff(filter="tcp port 80 and host " + socket.gethostbyname(socket.gethostname()),
                         timeout=30, count=0)
    keywords = ['GET', 'Host', 'Referer']
    output = []

    for packet in sniffed_data:
        packet_arrival_time = str(datetime.fromtimestamp(packet.time))

        # TODO: don't loop again if word was found. Splitting the packet into a string array may need to happen
        for keyword in keywords:
            if keyword in str(packet):
                # print(str(packet))
                # print('The keyword ' + keyword + ' was found at ' + packet_arrival_time)

                for objectionable_word in constants.objectionable_words_list:
                    if objectionable_word in str(packet):
                        output.append('The keyword ' + objectionable_word + ' was found at ' + packet_arrival_time)

    if not output:
        first_packet_time = str(datetime.fromtimestamp(sniffed_data[0].time))
        last_packet_time = str(datetime.fromtimestamp(sniffed_data[len(sniffed_data) - 1].time))
        output.append('No questionable words were found during ' + first_packet_time + last_packet_time + '.')

    return output
