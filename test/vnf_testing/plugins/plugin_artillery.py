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

    cmd = 'artillery quick '
    artillery_args_dict = {"count": 0,
                           "num": 0,
                           "target_ip": 0,
                           }

    if "count" in vnf_testing_args_dict:
        artillery_args_dict["count"] = str(vnf_testing_args_dict['count'])

    if "num" in vnf_testing_args_dict:
        artillery_args_dict["num"] = str(vnf_testing_args_dict['num'])

    if "target_ip" in vnf_testing_args_dict:
        artillery_args_dict["target_ip"] = str(vnf_testing_args_dict['target_ip'])
    else:
        artillery_args_dict["target_ip"] = "http://127.0.0.1/"

    for k, v in artillery_args_dict.items():
        if v != 0 and k != "target_ip":
            cmd = cmd + '--' + k + ' ' + str(v) + ' '

    cmd = cmd + str(artillery_args_dict["target_ip"])

    print("plugin_artillery : cmd = " + cmd)
    LOG.debug("plugin_artillery: cmd = " + cmd)

    # cmd = 'artillery quick --count 10 -n 20 http://192.168.8.101/'
    # cmd = 'artillery run artillery_config.yml'
    # artillery_config.yml transfer needed
    # vnf_testing_args_dict has the path of artillery_config.yml
    artillery_raw_result = listener.start_command(hosts=[hosts], auth=auth, command=cmd)

    artillery_result = artillery_raw_result.replace("\x1b[2K\x1b[1G\x1b[36m⠋\x1b[39m", "")
    artillery_result = artillery_result.replace("[192.168.9.211]", "")
    artillery_result = artillery_result.replace("out:", "")
    artillery_result = artillery_result.replace("\n", "")
    artillery_result = artillery_result.replace("\x1b[2K", "")
    artillery_result = artillery_result.replace("\x1b[1G", "")
    artillery_result = artillery_result.replace("\x1b[36m", "")
    artillery_result = artillery_result.replace("\x1b[39m", "")
    artillery_result = artillery_result.replace("\x1b[?25l", "")
    artillery_result = artillery_result.replace("\x1b[?25h", "")
    artillery_result = artillery_result.replace("⠙ ⠹ ⠸ ⠼ ⠴ ⠦ ⠧ ⠇ ⠏  ⠙ ⠹ ⠸ ⠼ ⠴ ⠦ ⠧ ⠇", "")

    print(artillery_result)
    return artillery_result
