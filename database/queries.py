from database.entities import *
from time import tzname


@db_session
def insert_packets(obj_packets_data):
    for obj_packet in obj_packets_data:
        date_received_value = obj_packet.get('Time')
        timezone_value = tzname[0]
        get_value = obj_packet.get('GET')
        host_value = obj_packet.get('Host')
        referer_value = obj_packet.get('Referer')

        db.insert('Packets', DateReceived=str(date_received_value), Timezone=timezone_value, Get=get_value,
                  Host=host_value, Referer=referer_value)

    commit()


@db_session
def get_packets():
    return select(p for p in Packets)[:]
