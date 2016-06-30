def remove_hex_values_from_packet(packet):
    """
    Splits the packet and removes all
    hex values from the packet via a
    known pattern of how the packet is
    formatted.

    :param packet: the packet in which
    to remove the hex values
    :return: a packet with no hex values
    """
    final_packet_list = []
    temp_packet_list = packet.split('\n')
    for value in temp_packet_list:
        try:
            final_packet_list.append(value.split('    ')[1].strip('\n'))
        except:
            pass

    packet_text_only = ''
    for value in final_packet_list:
        packet_text_only += value

    return packet_text_only


def parse_packet_data_by_keyword(packet, keyword):
    """
    Removes all of the data that's not
    relevant to the keyword parameter.

    :param packet: the packet in which
    to remove the irrelevant data
    :param keyword: the keyword that
    tells the method what to keep
    (e.g., the keyword would be 'GET',
    'HOST' or 'REFERER')
    :return: a packet with data that's
    relevant to the keyword parameter;
    an empty string if the parsing fails
    """
    try:
        if keyword != 'GET':
            return packet.split(keyword + ': ')[1].split('..')[0]

        return packet.split(keyword + ' ')[1].split(' ')[0]
    except:
        return ''
