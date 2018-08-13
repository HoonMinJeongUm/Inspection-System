# Monitoring Case_manager

from monitoring_manager.monitoring_manager import MonitoringManager
import logging

MonitorLog = logging.getLogger(__name__)


class MonitoringCaseManager(object):
    """
    Case management of monitoring
    """
    def __init__(self, request):
        """
        Initialize CaseManager
        1. type(vitrageconf) : starts vitrageconf module
        2. type(management) : starts management module
        :param request: 'request' must be an dictionary data type that includes header
        :returns: None
        """
        try:
            if request['header'] is not 'Monitoring':
                raise KeyError
        except KeyError:
            MonitorLog.error("Header is wrong. Please check again.")
        else:
            self.request = request
            if self.request['type'] is 'vitrageconf':
                self.start_vitrageconf()
            elif self.request['type'] is 'manager':
                self.start_management()
            else:
                MonitorLog.warning("Wrong data type. Please rewrite the type.")

    def start_vitrageconf(self):
        pass

    def start_management(self):
        """
        to do testing delete [self.request]
        :return: complete zabbix api result
        """
        MonitoringManager(self.request)


if __name__ == '__main__':
    requests = {'header': 'Monitoring', 'type': 'management'}
    MonitoringCaseManager(requests)
