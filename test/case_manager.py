# -*- coding: utf-8 -*-
# case_manager.py

from test.vim_testing import vim_test_manager
from test.vnf_testing import vnf_test_manager


class CaseManager(object):
    """Represents Case Manager's Functions
    """
    def __init__(self):
        pass

    def start(self, case):
        if str(case) == 'vim':
            pass
        elif str(case) == 'vnf':
            pass

