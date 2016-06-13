import subprocess
import sys
import os


def format_path(path, num_of_dirs_to_remove_from_path):
    formatted_path = path.split('/')

    for i in xrange(0, num_of_dirs_to_remove_from_path):
        del formatted_path[len(formatted_path) - 1]

    return '/'.join(formatted_path)


current_path = os.path.realpath(os.path.dirname(sys.argv[0]))
path_to_app = format_path(current_path, 1) + '/KeepInChecker/KeepInChecker'
subprocess.call('gksu --message "Please enter your password to run KeepInChecker" ' + path_to_app, shell=True)
