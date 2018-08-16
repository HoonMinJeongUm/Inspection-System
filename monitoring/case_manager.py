# Monitoring Case_manager

from monitoring_manager.monitoring_manager import MonitoringManager
from vitrageconf_manager.start_vitrageconf import VitrageconfManager
import logging, sys
import yaml

class MonitoringCaseManager(object):
    """
    Case management of monitoring
    """
    def __init__(self, request):
        self.MonitorLog = logging.getLogger("Monitoring Component")
        formatter = logging.Formatter('[%(levelname)s - %(name)s](%(asctime)s) : %(message)s')
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        self.MonitorLog.addHandler(handler)

        try:
            if request['header'] is not "Monitoring":
                raise KeyError
        except KeyError:
            self.MonitorLog.error("Header is wrong. Please check again.")
            sys.exit(1)
        else:
            self.request = request
            self.vitrage = VitrageconfManager(self.request)
            self.set_vitrage()
            self.start_management()
            self.start_vitrage_config()
            self.finish()

    def set_vitrage(self):
        """
        setting the zabbix configuration and send script to VM
        :return: None
        """
        self.vitrage.start_script()

    def start_vitrage_config(self):
        """
        setting the Vitrage between Zabbix connection, then restart the devstack service
        :return: None
        """
        self.vitrage.start_config()

    def start_management(self):
        """
        setting the Zabbix agent monitoring Item, trigger, graph, template to the Zabbix Server
        :return: None
        """
        MonitoringManager(self.request)

    def finish(self):
        pass


if __name__ == '__main__':
    with open("monitoring_data.yaml", 'r') as files:
        conf = yaml.load(files)
    MonitoringCaseManager(conf)