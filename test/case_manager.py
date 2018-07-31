# -*- coding: utf-8 -*-
# case_manager.py

from test.vim_testing import vim_test_manager
from test.vnf_testing import vnf_test_manager

import logging

LOG = logging.getLogger(__name__)


CASES = {'vim', 'vnf'}


class CaseManager(object):
    """Represents Case Manager's Functions.
    """
    def __init__(self):
        """Inits CaseManager."""
        pass

    @staticmethod
    def start(case, tool, hosts=None, auth=None, vnf_testing_args_dict=None, requestdict=None):
        """Starts every tools from plugins.

        Args:
            case: A string that decides whether vim testing or vnf testing.
            tool: A string that decides specific tools among testing plugins.
            hosts: A host's ip that user wants to test in.
            auth: A dictionary that contains host's hostname and password or public-key that user wants to test in.
            vnf_testing_args_dict: A dictionary of arguments used to execute the vnf testing plugins.
            requestdict: A dictionary that is used to execute the Rally testing.

        Returns:
            test_result: A string that is result of the test.
        """
        LOG.debug("Test-case_manager.py start()")
        if case not in CASES:
            # TODO(Jaewook) : Error Log.
            LOG.warning("The case is not in CASES set.")
            pass
        if str(case) == 'vim':
            LOG.debug("Test-case_manager.py start() - case 'vim'")
            test_result = vim_test_manager.start(tool, requestdict)
        elif str(case) == 'vnf':
            LOG.debug("Test-case_manager.py start() - case 'vim'")
            test_result = vnf_test_manager.start(tool, hosts, auth, vnf_testing_args_dict)

        return test_result

if __name__ == "__main__":
    logging.info('Starting logger for...')
    LOG = logging.getLogger(__name__)
    LOG.warning("Test-case_manager.py start()")
    CaseManager.start(case='vnf', tool='stressng', hosts='192.168.9.211', auth=['ubuntu', 'ubuntu'], vnf_testing_args_dict={"cpu": 2, "vm": 1, "vm_bytes": '1024m', "hdd": 1, "hdd_bytes": '1024m', "timeout": '10s'})
