# Use Zabbix Plugin
# Reference from Openstack Project [ Zabbix Plugin for Application Monitoring in Tacker VNF Manager ]

from monitoring_plugin.zabbix_plugin import VNFMonitorZabbix
import monitoring_plugin.zabbix_api as zapi
import time
import yaml
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
        self.name_of_template = "HoonMinJeongUm Template "

    def start(self, vnf, kwargs):
        self.__init__()
        self.read_yaml()
        self.add_to_appmonitor(vnf, kwargs)

    def read_yaml(self):
        with open('monitoring.yaml', 'r') as files:
            conf = yaml.load(files)
        self.kwargs = {'vdus': {'Name_of_host': {}}}
        self.kwargs['vdus']['Name_of_host'] = conf['app_monitoring_policy']

    def listen_testing(self):
        """
        listen the tessting result
        """
        pass

    def create_template(self):
        temp_template_api = copy.deepcopy(zapi.dTEMPLATE_CREATE_API)

        for vdu in self.vduname:
            temp_template_api['params']['host'] = self.name_of_template + str(vdu)
            temp_template_api['auth'] = \
                self.hostinfo[vdu]['zbx_info']['zabbix_token']
            response = self.send_post(temp_template_api)

            if 'error' in response:
                if "already exists." in response['error']['data']:
                    now = time.localtime()
                    rtime = str(now.tm_hour) + str(now.tm_min) + str(
                        now.tm_sec)
                    temp_template_api['params']['host'] = \
                        self.name_of_template + str(vdu) + rtime
                    response = self.send_post(temp_template_api)
                    VNFMonitorZabbix.check_error(response)
            self.hostinfo[vdu]['template_id'] = \
                response['result']['templateids']
            self.hostinfo[vdu]['template_name'] =\
                temp_template_api['params']['host']

    def add_to_appmonitor(self, vnf, kwargs):
        self.kwargs = kwargs
        self.vnf = vnf
        self.set_vdu_info()
        self.tenant_id = self.vnf['vnfd']['tenant_id']
        self.add_host_to_zabbix()
