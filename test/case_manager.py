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

    def start(self, case, tool, hosts=None, auth=None, vnf_testing_args_dict=None, requestdict=None):
        """Starts every tools from plugins.

        Args:
            case: A string that decides whether vim testing or vnf testing.
            tool: A string that decides specific tools among testing plugins.
            hosts: A host's ip that user wants to test in.
            auth: A host's password or public-key that user wants to test in.
            vnf_testing_args_dict: A dictionary of arguments used to execute the vnf testing plugins.
            requestdict: A dictionary that is used to execute the Rally testing.

        Returns:
            None.
        """
        LOG.debug("Test-case_manager.py start()")
        if case not in CASES:
            # TODO(Jaewook) : Error Log.
            LOG.warning("The case is not in CASES set.")
            pass
        if str(case) == 'vim':
            vim_test_manager.start(tool, requestdict)
        elif str(case) == 'vnf':
            vnf_test_manager.start(tool, hosts, auth, vnf_testing_args_dict)
