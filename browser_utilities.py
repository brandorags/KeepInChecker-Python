import command_line_utilities
import constants

from scapy.all import *
from datetime import datetime, timedelta


def is_browser_open():
    browsers = ['Firefox', 'Chrome', 'Safari', 'Opera']
    for browser in browsers:
        process = subprocess.Popen('ps -ax | grep ' + browser, stdout=subprocess.PIPE, shell=True)
        process_output = command_line_utilities.convert_output_to_string(process)
        for output in process_output:
            if 'app/Contents/MacOS'.lower() in output.lower():
                return True

    return False


def is_previous_packet_too_close_in_time_to_current_packet(obj_word,
                                                           current_obj_word_packet_arrival_time,
                                                           obj_words_found_datetimes):
    previous_obj_word_packet_arrival_time = obj_words_found_datetimes[obj_word]
    time_difference = current_obj_word_packet_arrival_time - previous_obj_word_packet_arrival_time

    if timedelta.total_seconds(time_difference) < 10:
        return True

    return False


def scan_user_internet_traffic():
    keywords = ['GET', 'Host', 'Referer']
    obj_words_found_datetimes = {}
    output = []

    time_at_beginning_of_scan = datetime.now()
    sniffed_data = sniff(filter="tcp port 80 and host " + socket.gethostbyname(socket.gethostname()),
                         timeout=60, count=0)
    for packet in sniffed_data:
        packet_arrival_time = datetime.fromtimestamp(packet.time)
        obj_word_found = False

        for keyword in keywords:
            if keyword in str(packet):
                for obj_word in constants.objectionable_words_list:
                    if obj_word in str(packet):
                        if obj_word in obj_words_found_datetimes and \
                                is_previous_packet_too_close_in_time_to_current_packet(obj_word,
                                                                                       packet_arrival_time,
                                                                                       obj_words_found_datetimes):
                            break

                        obj_word_found = True
                        obj_words_found_datetimes[obj_word] = packet_arrival_time
                        output.append('The word ' + obj_word + ' was found at ' + str(packet_arrival_time))
                        break

            if obj_word_found:
                break

    if not output:
        if sniffed_data:
            first_packet_time = str(datetime.fromtimestamp(sniffed_data[0].time))
            last_packet_time = str(datetime.fromtimestamp(sniffed_data[len(sniffed_data) - 1].time))
            output.append('No questionable words were found from ' + first_packet_time + ' to ' +
                          last_packet_time + '.')
        else:
            output.append('No questionable words were found from ' +
                          str(time_at_beginning_of_scan.strftime('%Y-%m-%d %H:%M:%S')) +
                          ' to ' + str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + '.')

    return output
