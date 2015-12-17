import browser_utilities
import command_line_utilities
import constants
import subprocess
import random

from emailer import Emailer
from time import sleep
from getpass import getpass


def show_welcome_message():
    print('\n---------- KeepInChecker v1.0 ----------')


def take_screenshot():
    subprocess.call('mkdir -p ' + constants.screenshot_file_path, shell=True)
    subprocess.call('screencapture ' + constants.screenshot_file_name, shell=True)


def delete_screenshot():
    subprocess.call('rm -rf ' + constants.screenshot_file_path, shell=True)


def mute_volume():
    subprocess.call("osascript -e 'set volume output muted true'", shell=True)


def unmute_volume():
    sleep(0.5)
    subprocess.call("osascript -e 'set volume output muted false'", shell=True)


def record_internet_traffic():
    command_line_utilities.initiate_tcpdump()


def main():
    show_welcome_message()
    sender = input('Your Email Address: ')
    sender_password = getpass('Your Password: ')
    recipient = input('Your Accountability Partner\'s Email Address: ')
    emailer = Emailer(sender, recipient,
                      sender_password, 'KeepInChecker Attachment',
                      Emailer.get_body_text(), constants.screenshot_file_name)

    mute_volume()
    take_screenshot()
    unmute_volume()
    emailer.send_email()
    delete_screenshot()


try:
    # while True:
    #     interval = random.randint(60, 240)
    #     sleep(interval)
    if browser_utilities.is_browser_open():
        # record_internet_traffic()
        main()
except:
    raise
