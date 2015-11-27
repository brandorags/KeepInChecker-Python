import subprocess
import time

from command_line_utilities import CommandLineUtilities


def take_screenshot():
    date = CommandLineUtilities.convert_output_to_string(subprocess.Popen('date', stdout=subprocess.PIPE))
    date = '-'.join(date.split(' '))
    subprocess.call('mkdir -p ~/TempFolder/TempFolder/TempScreenshotDirectory', shell=True)
    subprocess.call('screencapture ~/TempFolder/TempFolder/TempScreenshotDirectory/Screenshot-' +
                    date + '.png', shell=True)


def delete_screenshot():
    subprocess.call('rm -rf ~/TempFolder/TempFolder/TempScreenshotDirectory', shell=True)


def mute_volume():
    subprocess.call("osascript -e 'set volume output muted true'", shell=True)


def unmute_volume():
    time.sleep(1)
    subprocess.call("osascript -e 'set volume output muted false'", shell=True)


def main():
    mute_volume()
    take_screenshot()
    unmute_volume()
    delete_screenshot()


main()
