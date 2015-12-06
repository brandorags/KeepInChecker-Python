import browser_utilities
import subprocess
import random

from emailer import Emailer
from time import sleep
from sys import argv


def get_screenshot_file_path():
    return '/Users/Brando/TempFolder/TempFolder/TempScreenshotDirectory'


def get_screenshot_file_name():
    return '/Users/Brando/TempFolder/TempFolder/TempScreenshotDirectory/Screenshot.png'


def take_screenshot():
    subprocess.call('mkdir -p ' + get_screenshot_file_path(), shell=True)
    subprocess.call('screencapture ' + get_screenshot_file_name(), shell=True)


def delete_screenshot():
    subprocess.call('rm -rf ' + get_screenshot_file_path(), shell=True)


def mute_volume():
    subprocess.call("osascript -e 'set volume output muted true'", shell=True)


def unmute_volume():
    sleep(0.5)
    subprocess.call("osascript -e 'set volume output muted false'", shell=True)


def main():
    sender = argv[1]
    recipient = argv[2]
    sender_password = argv[3]
    emailer = Emailer(sender, recipient,
                      sender_password, 'KeepInChecker Attachment',
                      Emailer.get_body_text(), get_screenshot_file_name())

    mute_volume()
    take_screenshot()
    unmute_volume()
    emailer.send_email()
    delete_screenshot()


# while True:
#     interval = random.randint(60, 240)
#     sleep(interval)
    if browser_utilities.is_browser_open():
        main()
