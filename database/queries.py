from database.db_session import DbSession
from constants import constants, secret_key
from utilities import security_utilities
from time import tzname


def save_user_data(user_name, user_email, user_email_password,
                   partner_emails, email_frequency):
    current_user = get_current_user()
    if current_user:
        update_user_data(current_user, user_name, user_email,
                         user_email_password, partner_emails, email_frequency)
        return

    encrypted_password = security_utilities.encode(user_email_password, secret_key.key)

    db = DbSession()
    sql = 'INSERT INTO Users (UserName, UserEmail, UserEmailPassword, PartnerEmails, EmailFrequency) ' \
          'VALUES(\'' + user_name + '\'' + ',\'' + user_email + '\'' + ',\'' + encrypted_password + '\'' + \
          ',\'' + partner_emails + '\'' + ',\'' + email_frequency + '\')'

    db.cursor.execute(sql)
    db.commit()
    db.close()

    constants.current_user = get_current_user()


def update_user_data(existing_user, user_name, user_email, user_email_password,
                     partner_emails, email_frequency):
    db = DbSession()
    sql = 'UPDATE Users SET'
    update_values = ''
    needs_update = False

    if existing_user['UserName'] != user_name:
        update_values += ' UserName = \'' + user_name + '\','
        needs_update = True

    if existing_user['UserEmail'] != user_email:
        update_values += ' UserEmail = \'' + user_email + '\','
        needs_update = True

    if security_utilities.decode(existing_user['UserEmailPassword'], secret_key.key) != user_email_password:
        encrypted_password = security_utilities.encode(user_email_password, secret_key.key)
        update_values += ' UserEmailPassword = \'' + encrypted_password + '\','
        needs_update = True

    if existing_user['PartnerEmails'] != partner_emails:
        update_values += ' PartnerEmails = \'' + partner_emails + '\','
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
        date_received_value = obj_packet.get('Time')
        timezone_value = tzname[0]
        get_value = obj_packet.get('GET')
        host_value = obj_packet.get('Host')
        referer_value = obj_packet.get('Referer')

        sql = 'INSERT INTO Packets (DateReceived, Timezone, Get, Host, Referer)' \
              ' VALUES(\'' + str(date_received_value) + '\'' + ',' + \
              '\'' + timezone_value + '\',' + '\'' + get_value + '\',' + \
              '\'' + host_value + '\',' + '\'' + referer_value + '\')'

        db.cursor.execute(sql)

    db.commit()
    db.close()


def get_packets():
    db = DbSession()
    packets = db.cursor.execute('SELECT * FROM Packets')

    db.close()

    return packets


def get_current_user():
    db = DbSession()
    db.cursor.execute('SELECT * FROM Users')
    current_user = db.cursor.fetchone()

    db.close()

    return current_user
