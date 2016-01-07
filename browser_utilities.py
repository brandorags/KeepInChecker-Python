import command_line_utilities
import subprocess
import socket

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
                         timeout=5, count=0)
    keywords = ['GET', 'Host', 'Referer']

    for packet in sniffed_data:
        packet_arrival_time = str(datetime.fromtimestamp(packet.time))

        for keyword in keywords:
            if keyword in str(packet):
                print(str(packet))
                print('The keyword ' + keyword + ' was found at ' + packet_arrival_time)
