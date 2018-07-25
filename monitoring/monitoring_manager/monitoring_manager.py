# Use Zabbix Plugin
# Reference from Openstack Project [ Zabbix Plugin for Application Monitoring in Tacker VNF Manager ]

from monitoring_plugin.zabbix_plugin import VNFMonitorZabbix
import monitoring_plugin.zabbix_api as zapi
import time
import ConfigParser
import logging, sys
import yaml
import copy


class MonitoringManager(VNFMonitorZabbix):
    """
    Monitoring Manager
    """
    def __init__(self):
        super(MonitoringManager, self).__init__()
        self.data = None
        self.name_of_template = "HoonMinJeongUm Template "

    def start(self, vnf):
        """
        starts the main logic
        :param vnf: I have to fix it later..
        :return: none
        """
        self.__init__()
        self.read_yaml()
        self.add_to_appmonitor(vnf)

    def read_yaml(self):
        with open('monitoring.yaml', 'r') as files:
            conf = yaml.load(files)
        my_conf = self.parse_conf(conf)
        self.kwargs = {'vdus': {'Name_of_host': {}}}
        self.kwargs['vdus']['Name_of_host'] = my_conf['app_monitoring_policy']

    def parse_conf(self, conf):
        """
        parse the .cfg file into my conf file
        :param conf: default conf file
        :return: completed conf file
        """
        config = ConfigParser.ConfigParser()
        config.read('monitoring.cfg')
        #check for information section is correct
        try:
            for text in config.sections():
                if text != "INFO" and text != "APP" and text != "OS":
                    raise KeyError
        except KeyError:
            logging.error("Missing Information of Zabbix API")
            sys.exit(1)
        # parse the information
        conf['app_monitoring_policy']['zabbix_username'] = config.get('INFO', 'zabbix_username')
        conf['app_monitoring_policy']['zabbix_password'] = config.get('INFO', 'zabbix_password')
        conf['app_monitoring_policy']['zabbix_server_ip'] = config.get('INFO', 'zabbix_server_ip')
        conf['app_monitoring_policy']['zabbix_server_port'] = config.get('INFO', 'zabbix_server_port')
        conf['app_monitoring_policy']['mgmt_ip'] = config.get('INFO', 'mgmt_ip')
        conf['app_monitoring_policy']['parameters']['application']['app_name'] \
            = config.get('APP', 'app_name')
        conf['app_monitoring_policy']['parameters']['application']['app_port'] \
            = config.get('APP', 'app_port')
        conf['app_monitoring_policy']['parameters']['application']['ssh_username'] \
            = config.get('APP', 'ssh_username')
        conf['app_monitoring_policy']['parameters']['application']['ssh_password'] \
            = config.get('APP', 'ssh_password')
        # parse the application information
        app_status = config.get('APP', 'app_status')
        if app_status == "true":
            conf['app_monitoring_policy']['parameters']['application']['app_status']['actionname'] = 'cmd'
            conf['app_monitoring_policy']['parameters']['application']['app_status']['cmd-action'] \
                = 'sudo service apache2 restart'
            conf['app_monitoring_policy']['parameters']['application']['app_status']['condition'] \
                = ['down']
        else:
            del conf['app_monitoring_policy']['parameters']['application']['app_status']

        app_memory = config.get('APP', 'app_memory')
        if app_memory == "true":
            pass
        else:
            del conf['app_monitoring_policy']['parameters']['application']['app_memory']
        #parse the os information
        os_cpu_usage = config.get('OS', 'os_cpu_usage')
        if os_cpu_usage == "true":
            conf['app_monitoring_policy']['parameters']['OS']['os_cpu_usage']['actionname'] = 'cmd'
            conf['app_monitoring_policy']['parameters']['OS']['os_cpu_usage']['cmd-action'] \
                = 'sudo reboot'
            conf['app_monitoring_policy']['parameters']['OS']['os_cpu_usage']['condition'] \
                = ['less', 30]
        else:
            del conf['app_monitoring_policy']['parameters']['OS']['os_cpu_usage']

        os_proc_value = config.get('OS', 'os_proc_value')
        if os_proc_value == "true":
            pass
        else:
            del conf['app_monitoring_policy']['parameters']['OS']['os_proc_value']

        os_cpu_load = config.get('OS', 'os_cpu_load')
        if os_cpu_load == "true":
            pass
        else:
            del conf['app_monitoring_policy']['parameters']['OS']['os_cpu_load']

        os_agent_info = config.get('OS', 'os_agent_info')
        if os_agent_info == "true":
            pass
        else:
            del conf['app_monitoring_policy']['parameters']['OS']['os_agent_info']

        return conf

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

    def add_to_appmonitor(self, vnf):
        self.vnf = vnf
        self.set_vdu_info()
        self.tenant_id = self.vnf['vnfd']['tenant_id']
        self.add_host_to_zabbix()
