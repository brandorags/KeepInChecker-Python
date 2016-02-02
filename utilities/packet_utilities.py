def parse_get_data(word, packet):
    split_packet = packet.split(word)[1].strip().split(' ')
    beginning_of_gdata = split_packet[0].split('\n')[0]
    end_of_gdata = ''
    index_of_gdata_portion = 0

    for i in range(0, len(split_packet)):
        if 'HTTP' in split_packet[i]:
            end_of_gdata = split_packet[i].split('HTTP')[0]
            break
        elif index_of_gdata_portion == 11:
            beginning_of_gdata += split_packet[i].split('\n')[0]
            index_of_gdata_portion = 0

        index_of_gdata_portion += 1

    return beginning_of_gdata + end_of_gdata


def parse_host_data(word, packet):
    split_packet = packet.split(word + ':')[1].strip().split(' ')
    beginning_of_hdata = split_packet[0].split('\n')[0]
    end_of_hdata = ''
    index_of_hdata_portion = 0

    for i in range(0, len(split_packet)):
        if '..User' in split_packet[i]:
            end_of_hdata = split_packet[i].split('..User')[0]
            break
        elif index_of_hdata_portion == 11:
            beginning_of_hdata += split_packet[i].split('\n')[0]
            index_of_hdata_portion = 0

        index_of_hdata_portion += 1

    return beginning_of_hdata + end_of_hdata


def parse_referer_data(word, packet):
    split_packet = packet.split(word + ':')[1].strip().split(' ')
    beginning_of_rdata = split_packet[0].split('\n')[0]
    end_of_rdata = ''
    index_of_rdata_portion = 0

    for i in range(0, len(split_packet)):
        if '..Cookie' in split_packet[i]:
            end_of_rdata = split_packet[i].split('..Cookie')[0]
            break
        elif index_of_rdata_portion == 11:
            beginning_of_rdata += split_packet[i].split('\n')[0]
            index_of_rdata_portion = 0

        index_of_rdata_portion += 1

    return beginning_of_rdata + end_of_rdata