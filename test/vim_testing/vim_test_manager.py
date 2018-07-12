# -*- coding: utf-8 -*-
# vim_test_manager.py

from test.vim_testing.plugins import plugin_rally
import logging
LOG = logging.getLogger(__name__)


def vim_test_manager():
    pass


def start(tool, requestdict):
    if str(tool) == 'rally':
        plugin_rally.start(requestdict)

