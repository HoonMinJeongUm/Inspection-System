# -*- coding: utf-8 -*-
# plugin_locustio.py

from locust import HttpLocust, TaskSet, task
from ssh_manager import listener
import subprocess
import logging
LOG = logging.getLogger(__name__)


# Bash Command Function for using bash shell
def bash_command(cmd):
    subprocess.Popen(['/bin/bash', '-c', cmd])


def start(hosts=None, auth=None, vnf_testing_args_dict=None):
    cmd = 'locust -f locustfile.py'
    # locustfile.py transfer needed
    listener.start_command(hosts=hosts, auth=auth, command=cmd)
