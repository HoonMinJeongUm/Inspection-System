import yaml


def bottleneck(ip1,ip2,mod1,mod2,test):
    _ip1 = str(ip1)
    _ip2 = str(ip2)
    _mod1 = str(mod1)
    _mod2 = str(mod2)
    _test = str(test)
    a = [_ip1,_ip2]
    b = [_mod1,_mod2]
    _test = _test.replace("*"," ")
    _test = _test.replace("_","|")
    c = [a,b,_test]
    return c

# def monitoring(tool, ip, port, pas, user, name, type, vm_ip, vm_id):
#     dic_a = {'header': 'Monitoring',
#              'type': 'vitrageconf',
#              'moitoring tool':  str(tool),
#              'servier_ip': str(ip),
#              'server_port': str(port),
#              'sever_pass': str(pas),
#              'server_user': str(user),
#              'host_name ': str(name),
#              'host_type': str(type),
#              'vm_ip': str(vm_ip),
#              'vm_id': str(vm_id)}
#     return dic_a

def monitoring_vitrageconf(header,type,monitoring_tool,server_ip,
                           server_port,server_pass,server_user,vm_ip,
                           vm_id,host_name,host_type):
    with open("monitoring_data.yaml", 'r') as files:
        conf = yaml.load(files)
    del conf['app_monitoring_policy']
    conf['Header'] = str(header)
    conf['type'] = str(type)
    conf['vitrage_conf_policy']['monitoring_tool'] = str(monitoring_tool)
    conf['vitrage_conf_policy']['server_ip'] = str(server_ip)
    conf['vitrage_conf_policy']['server_port'] = int(server_port)
    conf['vitrage_conf_policy']['server_pass'] = str(server_pass)
    conf['vitrage_conf_policy']['server_user'] = str(server_user)
    conf['vitrage_conf_policy']['vm_ip'] = str(vm_ip)
    conf['vitrage_conf_policy']['vm_id'] = str(vm_id)
    conf['vitrage_conf_policy']['host_name'] = str(host_name)
    conf['vitrage_conf_policy']['host_type'] = str(host_type)
    return conf
def monitoring_manager(header,type,
                       zabbix_username, zabbix_password, zabbix_server_ip, zabbix_server_port, mgmt_ip,
                       app_name, app_port, ssh_username, ssh_password, as_condition_com, as_condition_val, as_usage, am_condition_com, am_condition_val, am_usage,
                        oa_condition_com, oa_condition_val, oa_usage, op_condition_com, op_condition_val, op_usage, oc_condition_com, oc_condition_val, oc_usage, ocu_condition_com, ocu_condition_val, ocu_usage):
    with open("monitoring_data.yaml", 'r') as files:
        conf = yaml.load(files)
    del conf['vitrage_conf_policy']
    conf['Header'] = str(header)
    conf['type'] = str(type)

    conf['app_monitoring_policy']['name'] = 'zabbix'
    conf['app_monitoring_policy']['zabbix_username'] = str(zabbix_username)
    conf['app_monitoring_policy']['zabbix_password'] = str(zabbix_password)
    conf['app_monitoring_policy']['zabbix_server_ip'] = str(zabbix_server_ip)
    conf['app_monitoring_policy']['zabbix_server_port'] = int(zabbix_server_port)
    conf['app_monitoring_policy']['mgmt_ip'] = str(mgmt_ip)

    conf['app_monitoring_policy']['parameters']['application']['app_name'] = str(app_name)
    conf['app_monitoring_policy']['parameters']['application']['app_port'] = int(app_port)
    conf['app_monitoring_policy']['parameters']['application']['ssh_username'] = str(ssh_username)
    conf['app_monitoring_policy']['parameters']['application']['ssh_password'] = str(ssh_password)
    conf['app_monitoring_policy']['parameters']['application']['app_status']['condition'] = str(as_condition_com)
    conf['app_monitoring_policy']['parameters']['application']['app_status']['value'] = str(as_condition_val)
    conf['app_monitoring_policy']['parameters']['application']['app_status']['usage'] = str(as_usage)
    conf['app_monitoring_policy']['parameters']['application']['app_memory']['condition'] = str(am_condition_com)
    conf['app_monitoring_policy']['parameters']['application']['app_memory']['value'] = str(am_condition_val)
    conf['app_monitoring_policy']['parameters']['application']['app_memory']['usage'] = str(am_usage)

    conf['app_monitoring_policy']['parameters']['OS']['os_agent_info']['condition'] = str(oa_condition_com)
    conf['app_monitoring_policy']['parameters']['OS']['os_agent_info']['value'] = str(oa_condition_val)
    conf['app_monitoring_policy']['parameters']['OS']['os_agent_info']['usage'] = str(oa_usage)
    conf['app_monitoring_policy']['parameters']['OS']['os_proc_value']['condition'] = str(op_condition_com)
    conf['app_monitoring_policy']['parameters']['OS']['os_proc_value']['value'] = str(op_condition_val)
    conf['app_monitoring_policy']['parameters']['OS']['os_proc_value']['usage'] = str(op_usage)
    conf['app_monitoring_policy']['parameters']['OS']['os_cpu_load']['condition'] = str(oc_condition_com)
    conf['app_monitoring_policy']['parameters']['OS']['os_cpu_load']['value'] = str(oc_condition_val)
    conf['app_monitoring_policy']['parameters']['OS']['os_cpu_load']['usage'] = str(oc_usage)
    conf['app_monitoring_policy']['parameters']['OS']['os_cpu_usage']['condition'] = str(ocu_condition_com)
    conf['app_monitoring_policy']['parameters']['OS']['os_cpu_usage']['value'] = str(ocu_condition_val)
    conf['app_monitoring_policy']['parameters']['OS']['os_cpu_usage']['usage'] = str(ocu_usage)
    return conf

def test_auth(auth1,auth2):
    auth1_1 = str(auth1)
    auth2_2 = str(auth2)
    return [auth1_1, auth2_2]

def test_vnf_dict(tool,f_data1,f_data2,f_data3,f_data4,f_data5,f_data6):
    test_data = str(tool)
    if test_data == 'locustio':
        a = {'locustfile' : str(f_data1)}
    elif test_data == 'stressng' :
        a = {"cpu" : int(f_data1),
             "vm" : int(f_data2),
             "vm_bytes" : str(f_data3),
             "hdd" : int(f_data4),
             "hdd_bytes" : str(f_data5),
             "timeout" : str(f_data6)}
    elif test_data == 'artillery':
        a = {'count' : int(f_data1),
             'num' : int(f_data2),
             'target_ip' : str(f_data3)}
    return a