import command_line_utilities
import subprocess


def is_browser_open():
    browsers = ['Firefox', 'Chrome', 'Safari', 'Opera']
    for browser in browsers:
        process = subprocess.Popen('ps -ax | grep ' + browser, stdout=subprocess.PIPE, shell=True)
        process_output = command_line_utilities.convert_output_to_string(process)
        for output in process_output:
            if 'app/Contents/MacOS'.lower() in output.lower():
                return True

    return False
