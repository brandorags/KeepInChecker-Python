import sqlite3

from constants import constants
from time import tzname


def save_user_data(user_name, user_email, user_email_password,
                   partner_emails, email_frequency):
    current_user = get_current_user()
    if current_user:
        update_user_data(current_user, user_name, user_email,
                         user_email_password, partner_emails, email_frequency)
        return

    hashed_password = constants.cryptographer.encrypt(bytes(user_email_password))

    db = DbSession()
    sql = 'INSERT INTO Users (UserName, UserEmail, UserEmailPassword, PartnerEmails, EmailFrequency) ' \
          'VALUES(\'' + user_name + '\'' + ',\'' + user_email + '\'' + ',\'' + hashed_password + '\'' + \
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

    if existing_user['UserName'] != user_name:
        update_values += ' UserName = \'' + user_name + '\','

    if existing_user['UserEmail'] != user_email:
        update_values += ' UserEmail = \'' + user_email + '\','

    if constants.cryptographer.decrypt(bytes(existing_user['UserEmailPassword'])) != bytes(user_email_password):
        hashed_password = constants.cryptographer.encrypt(bytes(user_email_password))
        update_values += ' UserEmailPassword = \'' + hashed_password + '\','

    if existing_user['PartnerEmails'] != partner_emails:
        update_values += ' PartnerEmails = \'' + partner_emails + '\','

    if existing_user['EmailFrequency'] != email_frequency:
        update_values += ' EmailFrequency = \'' + email_frequency + '\''

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


class DbSession(object):

    def __init__(self):
        self.connection = sqlite3.connect('/Users/Brando/Repositories/Bitbucket/KeepInChecker/database/KeepInChecker.sqlite')
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()

    def commit(self):
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()

    def _get_column_count(self, table_name):
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()

        self.cursor.execute('SELECT * FROM ' + table_name)
        row = self.cursor.fetchone()

        self.connection.close()

        return len(row)
