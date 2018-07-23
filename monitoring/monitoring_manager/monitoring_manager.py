# Use Zabbix Plugin
# Reference from Openstack Project [ Zabbix Plugin for Application Monitoring in Tacker VNF Manager ]

from monitoring_plugin.zabbix_plugin import VNFMonitorZabbix
import monitoring_plugin.zabbix_api as zapi
import copy


class MonitoringManager(VNFMonitorZabbix):
    """
    Monitoring Manager
    """
    def __init__(self):
        self.data = None
        self.kwargs = None
        self.vnf = None
        self.vduname = []
        self.URL = None
        self.hostinfo = {}
        self.tenant_id = None

    def start(self, case_manager_msg):
        self.data = case_manager_msg



