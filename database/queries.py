from constants import constants
from database.entities import *
from time import tzname


@db_session
def save_user_data(user_name, user_email, user_email_password,
                   partner_emails, email_frequency):
    users = get_users()
    if users:
        # currently, we're only saving one user in the database, so
        # we'll always want the first instance (i.e., users[0])
        update_user_data(users[0], user_name, user_email,
                         user_email_password, partner_emails, email_frequency)
        return

    hashed_password = constants.cryptographer.encrypt(bytes(user_email_password))

    Users(UserName=user_name, UserEmail=user_email, UserEmailPassword=hashed_password,
          PartnerEmails=partner_emails, EmailFrequency=email_frequency)

    constants.current_user = get_users()[0]


@db_session
def update_user_data(existing_user, user_name, user_email, user_email_password,
                     partner_emails, email_frequency):
    if existing_user.UserName != user_name:
        existing_user.UserName = user_name

    if existing_user.UserEmail != user_email:
        existing_user.UserEmail = user_email

    if constants.cryptographer.decrypt(bytes(existing_user.UserEmailPassword)) != bytes(user_email_password):
        hashed_password = constants.cryptographer.encrypt(bytes(user_email_password))
        existing_user.UserEmailPassword = hashed_password

    if existing_user.PartnerEmails != partner_emails:
        existing_user.PartnerEmails = partner_emails

    if existing_user.EmailFrequency != email_frequency:
        existing_user.EmailFrequency = email_frequency

    constants.current_user = get_users()[0]


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


@db_session
def get_packets():
    return select(packet for packet in Packets)[:]


@db_session
def get_users():
    return select(user for user in Users)[:]
