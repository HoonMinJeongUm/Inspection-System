# -*- coding: utf-8 -*-
# plugin_stressng.py

from ssh_manager import listener

import subprocess
import logging


logging.info('Starting logger for...')
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


def start(hosts=None, auth=None, vnf_testing_args_dict={}):
    """Starts stress-ng tool.

    Args:
        hosts: A host's ip that user wants to test in.
        auth: A dictionary that contains host's hostname and password or public-key that user wants to test in.
        vnf_testing_args_dict: A dictionary of arguments used to execute the vnf testing plugins.

    Returns:
        stressng_result: A string that is result of the test.
    """
    LOG.debug("plugin_stressng.py start()")
    cmd = 'stress-ng '
    stressng_args_dict = {"cpu": 0,
                          "vm": 0,
                          "vm-bytes": 0,
                          "hdd": 0,
                          "hdd-bytes": 0,
                          "timeout": 0,
                          }

    if "cpu" in vnf_testing_args_dict:
        stressng_args_dict["cpu"] = str(vnf_testing_args_dict['cpu'])

    if "vm" in vnf_testing_args_dict:
        stressng_args_dict["vm"] = str(vnf_testing_args_dict['vm'])

    if "vm_bytes" in vnf_testing_args_dict:
        stressng_args_dict["vm-bytes"] = str(vnf_testing_args_dict['vm_bytes'])

    if "hdd" in vnf_testing_args_dict:
        stressng_args_dict["hdd"] = str(vnf_testing_args_dict['hdd'])

    if "hdd_bytes" in vnf_testing_args_dict:
        stressng_args_dict["hdd-bytes"] = str(vnf_testing_args_dict['hdd_bytes'])

    if "timeout" in vnf_testing_args_dict:
        stressng_args_dict["timeout"] = str(vnf_testing_args_dict['timeout'])

    for k, v in stressng_args_dict.items():
        if v != 0:
            cmd = cmd + '--' + k + ' ' + str(v) + ' '

    cmd = cmd + '--metrics-brief'
    print("plugin_stressng : cmd = " + cmd)
    LOG.debug("plugin_stressng : cmd = " + cmd)

    # cmd = 'stress --cpu 4 --vm 3 --vm-bytes 2048m --hdd 2 --hdd-bytes 1024m --timeout 10s'
    stressng_result = listener.start_command(hosts=[hosts], auth=auth, command=cmd)

    return stressng_result
