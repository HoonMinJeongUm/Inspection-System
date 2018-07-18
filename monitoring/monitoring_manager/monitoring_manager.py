<<<<<<< Updated upstream
# Use Zabbix Plugin
# Reference from Openstack Project [ Zabbix Plugin for Application Monitoring in Tacker VNF Manager ]

from ..monitoring_plugin.zabbix_plugin import VNFMonitorZabbix


class MonitoringManager(VNFMonitorZabbix):
    """
    Monitoring Manager
    """
    def __init__(self):
        self.data = None

    def start(self, case_manager_msg):
        self.data = case_manager_msg
=======


>>>>>>> Stashed changes
