# Monitoring Case_manager

from monitoring_manager.monitoring_manager import MonitoringManager
from vitrageconf_manager.start_vitrageconf import VitrageconfManager
import logging
import yaml


MonitorLog = logging.getLogger("MonitorLog")


class MonitoringCaseManager(object):
    """
    Case management of monitoring
    """
    def __init__(self, request):
        try:
            if request['header'] is not "Monitoring":
                raise KeyError
        except KeyError:
            MonitorLog.error("Header is wrong. Please check again.")
        else:
            self.request = request
            a = VitrageconfManager(request)
            a.start_script()
            self.start_management()
            a.start_config()
            self.finish()

    def start_management(self):
        """
        to do testing delete [self.request]
        :return: complete zabbix api result
        """
        MonitoringManager(self.request)

    def finish(self):
        pass


if __name__ == '__main__':
    with open("test_monitoring.yaml", 'r') as files:
        conf = yaml.load(files)
    conf['header'] = 'Monitoring'
    MonitoringCaseManager(conf)


