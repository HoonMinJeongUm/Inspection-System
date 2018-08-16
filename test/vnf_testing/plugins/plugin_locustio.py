# -*- coding: utf-8 -*-
# plugin_locustio.py

from ssh_manager import listener

import subprocess
import logging

LOG = logging.getLogger(__name__)


# Bash Command Function for using bash shell
def bash_command(cmd):
    """Execute CLI command on /bin/bash shell.

    Args:
        cmd: A string that contains command to execute.

    Returns:
        None.
    """
    subprocess.Popen(['/bin/bash', '-c', cmd])


def start(hosts=None, auth=None, vnf_testing_args_dict=None):
    """Starts locustio tool.

    Args:
        hosts: A host's ip that user wants to test in.
        auth: A dictionary that contains host's hostname and password or public-key that user wants to test in.
        vnf_testing_args_dict: A dictionary of arguments used to execute the vnf testing plugins.

    Returns:
        locustio_result: A string that is locustio url.
    """
    LOG.debug("plugin_locustio.py start()")
    locustio_args_dict = {"locustfile": 'from locust import Locust, TaskSet, task\nclass MyTaskSet(TaskSet):\n\t@task\n\tdef my_task(self):\n\t\tprint("executing my_task")\n\nclass MyLocust(Locust):\n\ttask_set = MyTaskSet\n\tmin_wait = 5000\n\tmax_wait = 15000',
                        }

    if "locustfile" in vnf_testing_args_dict:
        locust_string = str(vnf_testing_args_dict['locustfile']).replace("NL", "\n")
        locustio_args_dict["locustfile"] = str(vnf_testing_args_dict['locustfile'])

    # get locustfile manually, and make locustfile with start_command
    cmd = 'echo "{0}" >> locustfile.py'.format(locustio_args_dict["locustfile"])
    listener.start_command(hosts=[hosts], auth=auth, command=cmd)

    # vnf_testing_args_dict has the path of locustfile.py
    cmd = 'locust -f locustfile.py'
    listener.start_command(hosts=[hosts], auth=auth, command=cmd)
    # TODO(Jaewook) : How to open new tab for locustio gui page?
    locustio_result = "http://{0}:5559".format(hosts)

    print(locustio_result)

    return locustio_result
