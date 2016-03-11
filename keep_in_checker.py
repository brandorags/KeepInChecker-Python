import random
import threading

from utilities import browser_utilities, email_utilities
from datetime import datetime
from database import queries
from multiprocessing import Queue
from constants import constants
from time import sleep


def initialize_current_user():
    users = queries.get_users()
    if users:
        constants.current_user = users[0]


def record_internet_traffic():
    internet_traffic_queue = Queue()
    thread = threading.Thread(target=browser_utilities.scan_user_internet_traffic,
                              args=(internet_traffic_queue,))
    thread.start()

    return internet_traffic_queue.get()


def send_scheduled_email():
    email_frequency = 1 if constants.current_user.EmailFrequency == 'Daily' else 7
    time_of_last_email_sent_to_now = datetime.now() - email_utilities.date_last_email_was_sent

    if time_of_last_email_sent_to_now.days == email_frequency:
        email_utilities.has_email_been_sent = False

    if not email_utilities.has_email_been_sent:
        email_utilities.send_email(constants.current_user.UserName, constants.current_user.UserEmail,
                                   constants.cryptographer.decrypt(bytes(constants.current_user.UserEmailPassword)),
                                   constants.current_user.PartnerEmails)

        email_utilities.has_email_been_sent = True
        email_utilities.date_last_email_was_sent = datetime.now()


def main():
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
