import random
import threading

from utilities import browser_utilities, email_utilities
from database import queries
from multiprocessing import Queue
from time import sleep


def record_internet_traffic():
    internet_traffic_queue = Queue()
    thread = threading.Thread(target=browser_utilities.scan_user_internet_traffic,
                              args=(internet_traffic_queue,))
    thread.start()

    return internet_traffic_queue.get()


def main():
    user = queries.get_users()
    if not browser_utilities.is_browser_open() and not user[0]:
        return

    internet_traffic = record_internet_traffic()

    if internet_traffic:
        for item in internet_traffic:
            print(item)

    # email_utilities.send_email(user_name, user_email, user_password, recipient_email)


# while True:
#     interval = random.randint(60, 240)
#     sleep(interval)