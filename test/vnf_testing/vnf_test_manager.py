# -*- coding: utf-8 -*-
# vnf_test_manager.py

from test.vnf_testing.plugins import plugin_locustio, plugin_stressng
import logging
LOG = logging.getLogger(__name__)


def vnf_test_manager():
    pass


def start(tool):
    if str(tool) == 'locustio':
        plugin_locustio.start()
    elif str(tool) == 'stress-ng':
        plugin_stressng.start()
