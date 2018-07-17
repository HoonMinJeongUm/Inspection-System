# -*- coding: utf-8 -*-
# plugin_stressng.py

from ssh_manager import listener
import subprocess
import logging
LOG = logging.getLogger(__name__)


# Bash Command Function for using bash shell
def bash_command(cmd):
    subprocess.Popen(['/bin/bash', '-c', cmd])


def start(hosts=None, auth=None):
    cmd = 'stress -c 4 --vm 3 --vm-bytes 2048m --hdd 2 --hdd-bytes 1024m'
    listener.start_command(hosts=hosts, auth=auth, command=cmd)
