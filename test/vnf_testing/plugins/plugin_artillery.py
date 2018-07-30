# -*- coding: utf-8 -*-
# plugin_artillery.py

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
    """Starts artillery tool.

    Args:
        hosts: A host's ip that user wants to test in.
        auth: A host's password or public-key that user wants to test in.
        vnf_testing_args_dict: A dictionary of arguments used to execute the vnf testing plugins.

    Returns:
        artillery_result: A string that is result of the test.
    """
    LOG.debug("plugin_artillery.py start()")
    cmd = 'artillery quick --count 10 -n 20 http://192.168.8.101/'
    # cmd = 'artillery run artillery_config.yml'
    # artillery_config.yml transfer needed
    # vnf_testing_args_dict has the path of artillery_config.yml
    artillery_result = listener.start_command(hosts=[hosts], auth=auth, command=cmd)

    return artillery_result
