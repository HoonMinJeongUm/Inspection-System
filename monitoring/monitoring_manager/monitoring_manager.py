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

    def set_vdu_info(self):
        temp_vduname = self.kwargs['vdus'].keys()
        for node in temp_vduname:
            if 'application' in \
                    self.kwargs['vdus'][node]['parameters'].keys():
                self.vduname.append(node)
                self.hostinfo[node] = copy.deepcopy(zapi.dVDU_INFO)
                self.set_zbx_info(node)
                self.hostinfo[node]['mgmt_ip'] = \
                    self.kwargs['vdus'][node]['mgmt_ip']
                self.hostinfo[node]['parameters'] = \
                    self.kwargs['vdus'][node]['parameters']
                self.hostinfo[node]['vdu_id'] = self.vnf['id']

