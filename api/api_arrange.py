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

def monitoring_manager(tool,ip,port,pwd,user,vm_ip,vm_id,host_name,host_type,vm_interface,app_name,app_port,ssh_username,ssh_password,as_c_c,as_c_u,am_c_c,am_c_v,am_c_u,oai_c_c,oai_c_u,opv_c_c,opv_c_v,opv_c_u,ocl_c_c,ocl_c_v,ocl_c_u,ocu_c_c,ocu_c_v,ocu_c_u):
    with open("monitoring_data.yaml", 'r') as files:
        conf = yaml.load(files)
    conf['header'] = 'Monitoring'
    conf['vitrage_conf_policy']['monitoring_tool'] = str(tool)
    conf['vitrage_conf_policy']['server_ip'] = str(ip)
    conf['vitrage_conf_policy']['server_port'] = int(port)
    conf['vitrage_conf_policy']['server_pass'] = str(pwd)
    conf['vitrage_conf_policy']['server_user'] = str(user)
    conf['vitrage_conf_policy']['vm_ip'] = str(vm_ip)
    conf['vitrage_conf_policy']['vm_id'] = str(vm_id)
    conf['vitrage_conf_policy']['host_name'] = str(host_name)
    conf['vitrage_conf_policy']['host_type'] = str(host_type)
    vm_interface=str(vm_interface)
    vm_interface=vm_interface.replace("*", "/")
    conf['vitrage_conf_policy']['vm_interface'] = vm_interface

    conf['app_monitoring_policy']['name'] = 'zabbix'
    conf['app_monitoring_policy']['host_name'] = str(host_name)
    conf['app_monitoring_policy']['zabbix_username'] = str(host_name)
    conf['app_monitoring_policy']['zabbix_password'] = str(pwd)
    conf['app_monitoring_policy']['zabbix_server_ip'] = str(ip)
    conf['app_monitoring_policy']['zabbix_server_port'] = int(port)
    conf['app_monitoring_policy']['mgmt_ip'] = str(vm_ip)
    conf['app_monitoring_policy']['parameters']['application']['app_name'] = str(app_name)
    conf['app_monitoring_policy']['parameters']['application']['app_port'] = int(app_port)
    conf['app_monitoring_policy']['parameters']['application']['ssh_username'] = str(ssh_username)
    conf['app_monitoring_policy']['parameters']['application']['ssh_password'] = str(ssh_password)
    conf['app_monitoring_policy']['parameters']['application']['app_status']['condition'] = [str(as_c_c)]
    conf['app_monitoring_policy']['parameters']['application']['app_status']['usage'] = [str(as_c_u)]
    conf['app_monitoring_policy']['parameters']['application']['app_memory']['condition'] = [str(am_c_c),int(am_c_v)]
    conf['app_monitoring_policy']['parameters']['application']['app_memory']['usage'] = [str(am_c_u)]
    conf['app_monitoring_policy']['parameters']['OS']['os_agent_info']['condition'] = [str(oai_c_c)]
    conf['app_monitoring_policy']['parameters']['OS']['os_agent_info']['usage'] = [str(oai_c_u)]
    conf['app_monitoring_policy']['parameters']['OS']['os_proc_value']['condition'] = [str(opv_c_c),int(opv_c_v)]
    conf['app_monitoring_policy']['parameters']['OS']['os_proc_value']['usage'] = [str(opv_c_u)]
    conf['app_monitoring_policy']['parameters']['OS']['os_cpu_load']['condition'] = [str(ocl_c_c),int(ocl_c_v)]
    conf['app_monitoring_policy']['parameters']['OS']['os_cpu_load']['usage'] = [str(ocl_c_u)]
    conf['app_monitoring_policy']['parameters']['OS']['os_cpu_usage']['condition'] = [str(ocu_c_c),int(ocu_c_v)]
    conf['app_monitoring_policy']['parameters']['OS']['os_cpu_load']['usage'] = [str(ocu_c_u)]
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