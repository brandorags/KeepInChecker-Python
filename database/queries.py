from database.entities import *


@db_session
def insert_packet(date_of_packet, timezone, get, host, referer):
    Packets(DateRecieved=date_of_packet, Timezone=timezone, Get=get,
            Host=host, Referer=referer)
