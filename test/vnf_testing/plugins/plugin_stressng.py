# -*- coding: utf-8 -*-
# plugin_stressng.py

from ssh_manager import listener
import subprocess
import logging
LOG = logging.getLogger(__name__)


# Bash Command Function for using bash shell
def bash_command(cmd):
    subprocess.Popen(['/bin/bash', '-c', cmd])


def start(hosts=None, auth=None, vnf_testing_args_dict={}):
    cmd = 'stress '
    stressng_args_dict = {"cpu": 0,
                          "vm": 0,
                          "vm-bytes": 0,
                          "hdd": 0,
                          "hdd-bytes": 0,
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

    for k, v in stressng_args_dict.items():
        if v != 0:
            cmd = cmd + '--' + k + ' ' + v + ' '

    LOG.debug("plugin_stressng : cmd = " + cmd)

    # cmd = 'stress -c 4 --vm 3 --vm-bytes 2048m --hdd 2 --hdd-bytes 1024m'
    listener.start_command(hosts=hosts, auth=auth, command=cmd)
