from database.entities import *
from time import tzname


@db_session
def insert_packet(obj_packet):
    date_received = None
    timezone = tzname[0]
    get = None
    host = None
    referer = None

    if obj_packet['Time']:
        date_received = obj_packet['Time']

    if obj_packet['GET']:
        get = obj_packet['GET']

    if obj_packet['Host']:
        host = obj_packet['Host']

    if obj_packet['Referer']:
        referer = obj_packet['Referer']

    Packets(DateRecieved=str(date_received), Timezone=timezone, Get=get,
            Host=host, Referer=referer)
