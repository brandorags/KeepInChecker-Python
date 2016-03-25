def remove_hex_values_from_packet(packet):
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
    try:
        if keyword != 'GET':
            return packet.split(keyword + ': ')[1].split('..')[0]

        return packet.split(keyword + ' ')[1].split(' ')[0]
    except:
        return ''
