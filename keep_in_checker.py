import random
import threading

from utilities import browser_utilities, email_utilities
from database import queries
from multiprocessing import Queue
from constants import constants
from time import sleep


def record_internet_traffic():
    internet_traffic_queue = Queue()
    thread = threading.Thread(target=browser_utilities.scan_user_internet_traffic,
                              args=(internet_traffic_queue,))
    thread.start()

    return internet_traffic_queue.get()


def initialize_current_user():
    users = queries.get_users()
    if users:
        constants.current_user = users[0]


def main():
    initialize_current_user()
    if not browser_utilities.is_browser_open() or not constants.current_user:
        return

    internet_traffic = record_internet_traffic()
    if internet_traffic:
        for item in internet_traffic:
            print(item)

    email_utilities.send_email(constants.current_user.UserName, constants.current_user.UserEmail,
                               constants.cryptographer.decrypt(bytes(constants.current_user.UserEmailPassword)),
                               constants.current_user.PartnerEmails)


# while True:
#     interval = random.randint(60, 240)
#     sleep(interval)