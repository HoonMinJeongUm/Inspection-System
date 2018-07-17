# -*- coding: utf-8 -*-
# plugin_locustio.py

from locust import HttpLocust, TaskSet, task
import subprocess
import logging
LOG = logging.getLogger(__name__)


# Bash Command Function for using bash shell
def bash_command(cmd):
    subprocess.Popen(['/bin/bash', '-c', cmd])


def start():
    cmd = 'locust -f locustfile.py'
    bash_command(cmd)