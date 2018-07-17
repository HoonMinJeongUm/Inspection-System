# -*- coding: utf-8 -*-
# plugin_stressng.py

import subprocess
import logging
LOG = logging.getLogger(__name__)


# Bash Command Function for using bash shell
def bash_command(cmd):
    subprocess.Popen(['/bin/bash', '-c', cmd])


# Temporary Function for calling
def start_command(DESTINATION_IP, ID, PASSWORD, COMMAND):
    pass


def start():
    cmd = 'stress -c 4 --vm 3 --vm-bytes 2048m --hdd 2 --hdd-bytes 1024m'
    start_command('192.168.11.101', 'ubuntu', 'ubuntu', cmd)
