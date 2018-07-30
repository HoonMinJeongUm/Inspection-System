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
        locustio_result: A string that is result of the test.
    """
    LOG.debug("plugin_locustio.py start()")
    cmd = 'locust -f locustfile.py'
    # locustfile.py transfer needed
    # vnf_testing_args_dict has the path of locustfile.py
    locustio_result = listener.start_command(hosts=[hosts], auth=auth, command=cmd)
    # TODO(Jaewook) : How to open new tab for locustio gui page?
    return locustio_result
