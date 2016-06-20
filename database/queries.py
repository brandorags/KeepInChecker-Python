from utilities.security_utilities import encrypt, decrypt
from database.db_session import DbSession
from constants import constants
from time import tzname


def save_user_data(user_name, user_email, user_email_password,
                   partner_emails, email_frequency):
    current_user = get_current_user()
    if current_user:
        update_user_data(current_user, user_name, user_email,
                         user_email_password, partner_emails, email_frequency)
        return

    db = DbSession()
    sql = 'INSERT INTO User (UserName, UserEmail, UserEmailPassword, PartnerEmails, EmailFrequency) ' \
          'VALUES(\'' + encrypt(user_name) + '\'' + ',\'' + encrypt(user_email) + '\'' + ',\'' + \
          encrypt(user_email_password) + '\'' + ',\'' + encrypt(partner_emails) + '\'' + ',\'' + \
          encrypt(email_frequency) + '\')'

    db.cursor.execute(sql)
    db.commit()
    db.close()

    constants.current_user = get_current_user()


def update_user_data(existing_user, user_name, user_email, user_email_password,
                     partner_emails, email_frequency):
    db = DbSession()
    sql = 'UPDATE User SET'
    update_values = ''
    needs_update = False

    if existing_user['UserName'] != user_name:
        update_values += ' UserName = \'' + encrypt(user_name) + '\','
        needs_update = True

    if existing_user['UserEmail'] != user_email:
        update_values += ' UserEmail = \'' + encrypt(user_email) + '\','
        needs_update = True

    if decrypt(existing_user['UserEmailPassword']) != user_email_password:
        encrypted_password = encrypt(user_email_password)
        update_values += ' UserEmailPassword = \'' + encrypt(encrypted_password) + '\','
        needs_update = True

    if existing_user['PartnerEmails'] != partner_emails:
        update_values += ' PartnerEmails = \'' + encrypt(partner_emails) + '\','
        needs_update = True

    if existing_user['EmailFrequency'] != email_frequency:
        update_values += ' EmailFrequency = \'' + email_frequency + '\''
        needs_update = True

    if needs_update:
        update_values = update_values.strip(',')
        sql += update_values + ' WHERE UserId = 1'

        db.cursor.execute(sql)
        db.commit()
        db.close()

        constants.current_user = get_current_user()


def insert_packets(obj_packets_data):
    db = DbSession()

    for obj_packet in obj_packets_data:
        date_received_value = encrypt(obj_packet.get('Time'))
        timezone_value = tzname[0]
        get_value = encrypt(obj_packet.get('GET'))
        host_value = encrypt(obj_packet.get('Host'))
        referer_value = encrypt(obj_packet.get('Referer'))

        sql = 'INSERT INTO Packet (DateReceived, Timezone, Get, Host, Referer)' \
              ' VALUES(\'' + str(date_received_value) + '\'' + ',' + \
              '\'' + timezone_value + '\',' + '\'' + get_value + '\',' + \
              '\'' + host_value + '\',' + '\'' + referer_value + '\')'

        db.cursor.execute(sql)

    db.commit()
    db.close()


def get_packets():
    db = DbSession()
    packets = db.cursor.execute('SELECT * FROM Packet').fetchall()

    db.close()

    return packets


def get_current_user():
    db = DbSession()
    db.cursor.execute('SELECT * FROM User')
    current_user = db.cursor.fetchone()

    db.close()

    return current_user
