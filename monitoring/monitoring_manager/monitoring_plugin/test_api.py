from zabbix_plugin import VNFMonitorZabbix

test_vnf = {'vnfd': {'tenant_id': u'd1e6919c73074d18ab6cd49a02e08391'},
            'id': 'b9af3cb5-6e43-4b2c-a056-67bda3f71e1a'}
test_kwargs = {'vdus': {'VDU1':
                            {'parameters':
                                 {'application':
                                      {'app_name': 'apache2',
                                       'app_status': {'actionname': 'cmd',
                                                      'cmd-action': 'sudo service \
                                            apache2 restart',
                                                      'condition': ['down']},
                                       'ssh_username': 'ubuntu',
                                       'app_port': 80,
                                       'ssh_password': 'ubuntu'}},
                             'name': 'zabbix',
                             'zabbix_username': 'Admin',
                             'zabbix_password': 'zabbix',
                             'zabbix_server_ip': '192.168.11.53',
                             'zabbix_server_port': 80,
                             'mgmt_ip': '192.168.11.206'}}}

test = VNFMonitorZabbix()
test.add_to_appmonitor(test_vnf, test_kwargs)
print test_kwargs['vdus'].values()