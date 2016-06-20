import random
import threading

from utilities import browser_utilities, email_utilities
from utilities.security_utilities import decrypt
from constants import constants
from multiprocessing import Queue
from datetime import datetime
from database import queries
from time import sleep


def initialize_current_user():
    user = queries.get_current_user()
    if user:
        constants.current_user = user


def record_internet_traffic():
    internet_traffic_queue = Queue()
    thread = threading.Thread(target=browser_utilities.scan_user_internet_traffic,
                              args=(internet_traffic_queue,))
    thread.start()

    return internet_traffic_queue.get()


def send_scheduled_email():
    email_frequency = 1 if constants.current_user['EmailFrequency'] == 'Daily' else 7
    time_of_last_email_sent_to_now = datetime.now() - email_utilities.date_last_email_was_sent

    if time_of_last_email_sent_to_now.days == email_frequency:
        email_utilities.has_email_been_sent = False

    if not email_utilities.has_email_been_sent:
        # the UserEmailPassword value needs to be doubly decrypted;
        # as to why, I'm not sure yet
        email_utilities.send_email(decrypt(constants.current_user['UserName']),
                                   decrypt(constants.current_user['UserEmail']),
                                   decrypt(decrypt(constants.current_user['UserEmailPassword'])),
                                   decrypt(constants.current_user['PartnerEmails']))

        email_utilities.has_email_been_sent = True
        email_utilities.date_last_email_was_sent = datetime.now()


def main():
    initialize_current_user()

    while True:
        interval = random.randint(60, 240)
        sleep(interval)

        if not browser_utilities.is_browser_open() or not constants.current_user:
            return

        internet_traffic = record_internet_traffic()
        if internet_traffic:
            for item in internet_traffic:
                print(item)

        try:
            send_scheduled_email()
        except:
            pass
