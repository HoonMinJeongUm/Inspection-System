# Monitoring Case_manager

from monitoring_manager.monitoring_manager import MonitoringManager
from vitrageconf_manager import vitrage_configuration
import logging


class MonitoringCaseManager(object):
    """
    Case management of monitoring
    """
    def __init__(self, request):
        try:
            if request['header'] is not 'Monitoring':
                raise KeyError
        except KeyError:
            logging.error("Header is wrong. Please check again.")
        else:
            self.request = request
            if self.request['type'] is 'vitrageconf':
                self.start_vitrageconf()
            elif self.request['type'] is 'management':
                self.start_management()
            else:
                logging.warning("Wrong data type. Please rewrite the type.")

    def start_vitrageconf(self):
        pass

    def start_management(self):
        pass
