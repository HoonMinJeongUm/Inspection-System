# Use Zabbix Plugin
# Reference from Openstack Project [ Zabbix Plugin for Application Monitoring in Tacker VNF Manager ]

from monitoring_plugin.zabbix_plugin import VNFMonitorZabbix
import monitoring_plugin.zabbix_api as zapi
import time
import ConfigParser
import logging, sys
import copy
import ast
import yaml


class MonitoringManager(VNFMonitorZabbix):
    """
    Monitoring Manager
    """
    def __init__(self, request):
        super(MonitoringManager, self).__init__()
        self.ManagerLog = logging.getLogger("Monitoring Manager")
        formatter = logging.Formatter('[%(levelname)s - %(name)s](%(asctime)s) : %(message)s')
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        self.ManagerLog.addHandler(handler)

        self.my_conf = request
        self.mgmt_IP = self.my_conf['app_monitoring_policy']['mgmt_ip']
        self.host_name = self.my_conf['app_monitoring_policy']['host_name']
        self.name_of_template = "HoonMinJeongUm Template "

        self.start()
        self.complete()

    def start(self):
        """
        starts the main logic
        if it has many vm, register them all
        :return: none
        """
        self.read_data()
        for number in range(0, len(self.mgmt_IP)):
            self.my_conf['app_monitoring_policy']['mgmt_ip'] = self.mgmt_IP[number]
            self.kwargs = {'vdus': {self.host_name[number]: {}}}
            self.kwargs['vdus'][self.host_name[number]] = self.my_conf['app_monitoring_policy']
            print self.kwargs
            self.add_to_appmonitor()

    def read_data(self):
        """
        making data for zabbix_plugin
        to use monitoring [yaml] template
        :return: none
        """
        try:
            if not self.my_conf['app_monitoring_policy']:
                raise KeyError
        except KeyError:
            self.ManagerLog.error("No data for Monitoring manager")
            sys.exit(1)

        self.parse_status()
        # waiting for testing result
        # self.listen_testing()
        # self.data_check()
        # name_parse
        # self.name = self.my_conf['app_monitoring_policy']['host_name']
        del self.my_conf['app_monitoring_policy']['host_name']

    def parse_status(self):
        """
        Based by status information, this module write more information for zabbix_plugin
        :return:
        """
        # parse the application information
        if self.my_conf['app_monitoring_policy']['parameters']['application']['app_status']['usage'] == 'true':
            self.my_conf['app_monitoring_policy']['parameters']['application']['app_status']['actionname'] \
                 = 'cmd'
            self.my_conf['app_monitoring_policy']['parameters']['application']['app_status']['cmd-action'] \
                = 'sudo service bono restart'
            del self.my_conf['app_monitoring_policy']['parameters']['application']['app_status']['usage']
        else:
            del self.my_conf['app_monitoring_policy']['parameters']['application']['app_status']

        if self.my_conf['app_monitoring_policy']['parameters']['application']['app_memory']['usage'] == 'true':
            self.my_conf['app_monitoring_policy']['parameters']['application']['app_memory']['actionname'] \
                 = 'cmd'
            self.my_conf['app_monitoring_policy']['parameters']['application']['app_memory']['cmd-action'] \
                = 'sudo service bono restart'
            del self.my_conf['app_monitoring_policy']['parameters']['application']['app_memory']['usage']
        else:
            del self.my_conf['app_monitoring_policy']['parameters']['application']['app_memory']
        # parse the os information
        if self.my_conf['app_monitoring_policy']['parameters']['OS']['os_agent_info']['usage'] == 'true':
            self.my_conf['app_monitoring_policy']['parameters']['OS']['os_agent_info']['actionname'] = 'cmd'
            self.my_conf['app_monitoring_policy']['parameters']['OS']['os_agent_info']['cmd-action'] \
                = 'sudo service bono restart'
            del self.my_conf['app_monitoring_policy']['parameters']['OS']['os_agent_info']['usage']
        else:
            del self.my_conf['app_monitoring_policy']['parameters']['OS']['os_agent_info']

        if self.my_conf['app_monitoring_policy']['parameters']['OS']['os_proc_value']['usage'] == 'true':
            self.my_conf['app_monitoring_policy']['parameters']['OS']['os_proc_value']['actionname'] = 'cmd'
            self.my_conf['app_monitoring_policy']['parameters']['OS']['os_proc_value']['cmd-action'] \
                = 'sudo service bono restart'
            del self.my_conf['app_monitoring_policy']['parameters']['OS']['os_proc_value']['usage']
        else:
            del self.my_conf['app_monitoring_policy']['parameters']['OS']['os_proc_value']

        if self.my_conf['app_monitoring_policy']['parameters']['OS']['os_cpu_load']['usage'] == 'true':
            self.my_conf['app_monitoring_policy']['parameters']['OS']['os_cpu_load']['actionname'] = 'cmd'
            self.my_conf['app_monitoring_policy']['parameters']['OS']['os_cpu_load']['cmd-action'] \
                = 'sudo service bono restart'
            del self.my_conf['app_monitoring_policy']['parameters']['OS']['os_cpu_load']['usage']
        else:
            del self.my_conf['app_monitoring_policy']['parameters']['OS']['os_cpu_load']

        if self.my_conf['app_monitoring_policy']['parameters']['OS']['os_cpu_usage']['usage'] == 'true':
            self.my_conf['app_monitoring_policy']['parameters']['OS']['os_cpu_usage']['actionname'] = 'cmd'
            self.my_conf['app_monitoring_policy']['parameters']['OS']['os_cpu_usage']['cmd-action'] \
                = 'sudo service bono restart'
            del self.my_conf['app_monitoring_policy']['parameters']['OS']['os_cpu_usage']['usage']
        else:
            del self.my_conf['app_monitoring_policy']['parameters']['OS']['os_cpu_usage']

    @staticmethod
    def complete():
        print("=================================================================")
        print("                 Monitoring Manager Complete                     ")
        print("=================================================================")

    def listen_testing(self):
        """
        listen the testing result
        This module fix the self.my_conf reference from testing result
        :return: None
        """
        # temporary waiting time
        wait_for_testing_result = 1
        time.sleep(wait_for_testing_result)

        if self.my_conf['app_monitoring_policy']['parameters']['application'] is None \
                and self.my_conf['app_monitoring_policy']['parameters']['OS'] is None:
            return
        # test result must have some more information
        # here is the template of the code
        test_result = 3.3
        if 0 <= test_result < 5:
            pass
        elif test_result < 10:
            pass
        else:
            self.ManagerLogger.warning("Testing result is wrong. Not fix condition")

    def data_check(self):
        """
        before using zaabix_plugin check all data
        if data is wrong, print the log and program exit
        :return: None
        """
        for topic in self.my_conf['app_monitoring_policy']:
            try:
                if not self.my_conf['app_monitoring_policy'][topic]:
                    raise KeyError
            except KeyError:
                self.ManagerLog.error("Missing Key in [%s]" % topic)
                sys.exit(1)

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

    def set_vdu_info(self):
        temp_vduname = self.kwargs['vdus'].keys()
        for node in temp_vduname:
            if 'application' in \
                    self.kwargs['vdus'][node]['parameters'].keys() \
                    or 'OS' \
                    in self.kwargs['vdus'][node]['parameters'].keys():
                self.vduname.append(node)
                self.hostinfo[node] = copy.deepcopy(zapi.dVDU_INFO)
                self.set_zbx_info(node)
                self.hostinfo[node]['mgmt_ip'] = \
                    self.kwargs['vdus'][node]['mgmt_ip']
                self.hostinfo[node]['parameters'] = \
                    self.kwargs['vdus'][node]['parameters']

    def add_to_appmonitor(self):
        self.set_vdu_info()
        self.add_host_to_zabbix()


if __name__ == '__main__':
    with open("../monitoring_data.yaml", 'r') as files:
        conf = yaml.load(files)

    MonitoringManager(conf)
