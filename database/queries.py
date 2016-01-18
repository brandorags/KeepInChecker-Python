from database.entities import *
from time import tzname


@db_session
def insert_packets(obj_packets_data):
    for obj_packet in obj_packets_data:
        date_received_value = None
        timezone_value = tzname[0]
        get_value = None
        host_value = None
        referer_value = None

        if obj_packet['Time']:
            date_received_value = obj_packet['Time']

        if obj_packet['GET']:
            get_value = obj_packet['GET']

        if obj_packet['Host']:
            host_value = obj_packet['Host']

        if obj_packet['Referer']:
            referer_value = obj_packet['Referer']

        db.insert("Packets", DateReceived=str(date_received_value), Timezone=timezone_value, Get=get_value,
                  Host=host_value, Referer=referer_value)

    commit()
