from passlib.hash import pbkdf2_sha512
from database.entities import *
from time import tzname


@db_session
def insert_user(user_name, user_email, user_email_password,
                partner_email, email_frequency):
    hashed_password = pbkdf2_sha512.encrypt(user_email_password, rounds=40000, salt_size=16)

    Users(UserName=user_name, UserEmail=user_email, UserEmailPassword=hashed_password,
          PartnerEmail=partner_email, EmailFrequency=email_frequency)


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
