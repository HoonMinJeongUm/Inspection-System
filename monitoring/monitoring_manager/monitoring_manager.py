# Use Zabbix Plugin
# Reference from Openstack Project [ Zabbix Plugin for Application Monitoring in Tacker VNF Manager ]

from monitoring_plugin.zabbix_plugin import VNFMonitorZabbix
import monitoring_plugin.zabbix_api as zapi
import time
import ConfigParser
import logging, sys
import yaml
import copy
import ast


class MonitoringManager(VNFMonitorZabbix):
    """
    Monitoring Manager
    """
    def __init__(self):
        super(MonitoringManager, self).__init__()
        self.data = None
<<<<<<< HEAD
        self
=======
        self.name_of_template = "HoonMinJeongUm Template "
>>>>>>> e6c8515a0173b1344b3f245282b33c9ade813503

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
                if text != "INFO" and text!= "APP_INFO" and text != "APP" and text != "OS":
                    raise KeyError
        except KeyError:
            logging.error("Missing Information of Zabbix API")
            sys.exit(1)

        # parse the basic_information
        for INFO in config.options('INFO'):
            conf['app_monitoring_policy'][INFO] = config.get('INFO', INFO)
        # parse the app_information
        for APP_INFO in config.options('APP_INFO'):
            conf['app_monitoring_policy']['parameters']['application'][APP_INFO] \
                = config.get('APP_INFO', APP_INFO)
        # parse the application information
        for topic in config.options('APP'):
            parse_app = config.get('APP', topic)
            parse_app = ast.literal_eval(parse_app)
            if parse_app['status'] == "true":
                conf['app_monitoring_policy']['parameters']['application'][topic]['actionname'] \
                    = 'cmd'
                conf['app_monitoring_policy']['parameters']['application'][topic]['cmd-action'] \
                    = parse_app['cmd-action']
                conf['app_monitoring_policy']['parameters']['application'][topic]['condition'] \
                    = parse_app['condition']
            else:
                del conf['app_monitoring_policy']['parameters']['application'][topic]
        #parse the os information
        for topic in config.options('OS'):
            parse_os = config.get('OS', topic)
            parse_os = ast.literal_eval(parse_os)
            if parse_os['status'] == "true":
                conf['app_monitoring_policy']['parameters']['OS'][topic]['actionname'] = 'cmd'
                conf['app_monitoring_policy']['parameters']['OS'][topic]['cmd-action'] \
                    = parse_os['cmd-action']
                conf['app_monitoring_policy']['parameters']['OS'][topic]['condition'] \
                    = parse_os['condition']
            else:
                del conf['app_monitoring_policy']['parameters']['OS'][topic]

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
