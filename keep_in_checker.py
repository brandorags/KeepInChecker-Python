import random
import threading

from utilities import browser_utilities, email_utilities
from multiprocessing import Queue
from getpass import getpass
from time import sleep


def show_welcome_message():
    print('\n---------- KeepInChecker v1.0 ----------')


def record_internet_traffic():
    internet_traffic_queue = Queue()
    thread = threading.Thread(target=browser_utilities.scan_user_internet_traffic,
                              args=(internet_traffic_queue,))
    thread.start()

    return internet_traffic_queue.get()


def main():
    show_welcome_message()
    # user_name = raw_input('Your name: ')
    # user_email = raw_input('Your Email Address: ')
    # user_password = getpass('Your Password: ')
    # recipient_email = raw_input('Your Accountability Partner\'s Email Address: ')

    internet_traffic = record_internet_traffic()

    if internet_traffic:
        for item in internet_traffic:
            print(item)

    # email_utilities.send_email(user_name, user_email, user_password, recipient_email)


# while True:
#     interval = random.randint(60, 240)
#     sleep(interval)
if browser_utilities.is_browser_open():
    main()
