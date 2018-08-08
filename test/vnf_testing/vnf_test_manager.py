# -*- coding: utf-8 -*-
# vnf_test_manager.py

from test.vnf_testing.plugins import plugin_locustio
from test.vnf_testing.plugins import plugin_stressng
from test.vnf_testing.plugins import plugin_artillery

import logging


logging.info('Starting logger for...')

LOG = logging.getLogger(__name__)


def start(tool, hosts=None, auth=None, vnf_testing_args_dict=None):
    """Starts vnf testing tool from plugins.

    Args:
        tool: A string that decides specific tools among testing plugins.
        hosts: A host's ip that user wants to test in.
        auth: A dictionary that contains host's hostname and password or public-key that user wants to test in.
        vnf_testing_args_dict: A dictionary of arguments used to execute the vnf testing plugins.

    Returns:
        vnf_test_result: A string that is result of the test.
    """
    LOG.debug("vnf_test_manager.py start()")

    vnf_test_result = None

    if str(tool) == 'locustio':
        vnf_test_result = plugin_locustio.start(hosts, auth, vnf_testing_args_dict)
    elif str(tool) == 'stressng':
        vnf_test_result = plugin_stressng.start(hosts, auth, vnf_testing_args_dict)
    elif str(tool) == 'artillery':
        vnf_test_result = plugin_artillery.start(hosts, auth, vnf_testing_args_dict)

    return vnf_test_result
