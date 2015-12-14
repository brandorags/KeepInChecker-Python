import subprocess
import constants


def convert_output_to_string(output_object):
    """
    Returns a string representation of standard output from the command line. In order
    to remove the newline character, splitting it from the rest of the output is mandatory.

    :parameter output_object - a subprocess.Popopen object that contains the command output
    """
    return output_object.stdout.read().decode('utf-8').split('\n')


def initiate_tcpdump():
    subprocess.call('mkdir -p ' + constants.tcpdump_file_path, shell=True)
    subprocess.Popen('sudo tcpdump -s 0 -A "tcp[((tcp[12:1] & 0xf0) >> 2):4] = 0x47455420" > ' +
                     constants.tcpdump_file_name,
                     shell=True)
