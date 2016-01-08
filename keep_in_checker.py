import browser_utilities
import constants
import random

from emailer import Emailer
from time import sleep
from getpass import getpass


def show_welcome_message():
    print('\n---------- KeepInChecker v1.0 ----------')


def record_internet_traffic():
    return browser_utilities.scan_user_internet_traffic()


def main():
    show_welcome_message()
    # sender = input('Your Email Address: ')
    # sender_password = getpass('Your Password: ')
    # recipient = input('Your Accountability Partner\'s Email Address: ')

    internet_traffic = record_internet_traffic()

    for item in internet_traffic:
        print(item)

    # emailer = Emailer(sender, recipient,
    #                   sender_password, 'KeepInChecker Report',
    #                   constants.generate_body_text(internet_traffic))
    #
    # emailer.send_email()


# while True:
#     interval = random.randint(60, 240)
#     sleep(interval)
if browser_utilities.is_browser_open():
    # record_internet_traffic()
    main()
