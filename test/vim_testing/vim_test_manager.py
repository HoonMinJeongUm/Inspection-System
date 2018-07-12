# -*- coding: utf-8 -*-
# vim_test_manager.py

from test.vim_testing.plugins import plugin_rally
import logging
LOG = logging.getLogger(__name__)


def vim_test_manager():
    pass


def start(tool, **kwargs):
    if str(tool) == 'rally':
        if kwargs.has_key("requestdict"):
            plugin_rally.start(kwargs["requestdict"])

