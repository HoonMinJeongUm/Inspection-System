# -*- coding: utf-8 -*-
# vnf_test_manager.py

from test.vnf_testing.plugins import plugin_locustio
from test.vnf_testing.plugins import plugin_stressng
from test.vnf_testing.plugins import plugin_artillery

import logging

LOG = logging.getLogger(__name__)


def start(tool, hosts=None, auth=None, vnf_testing_args_dict=None):
    """Starts vnf testing tool from plugins.

    Args:
        tool: A string that decides specific tools among testing plugins.
        hosts: A host's ip that user wants to test in.
        auth: A host's password or public-key that user wants to test in.
        vnf_testing_args_dict: A dictionary of arguments used to execute the vnf testing plugins.

    Returns:
        None.
    """
    LOG.debug("vnf_test_manager.py start()")
    if str(tool) == 'locustio':
        plugin_locustio.start(hosts, auth, vnf_testing_args_dict)
    elif str(tool) == 'stress-ng':
        plugin_stressng.start(hosts, auth, vnf_testing_args_dict)
    elif str(tool) == 'artillery':
        plugin_artillery.start(hosts, auth, vnf_testing_args_dict)
