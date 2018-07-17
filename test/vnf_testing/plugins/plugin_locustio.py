# -*- coding: utf-8 -*-
# plugin_locustio.py

from locust import HttpLocust, TaskSet, task
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
    cmd = 'locust -f locustfile.py'
    start_command('192.168.9.101', 'ubuntu', 'ubuntu', cmd)