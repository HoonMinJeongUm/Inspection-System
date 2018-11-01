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


def monitoring_manager(encoded_data):
    with open("monitoring_data.yaml", 'r') as files:
        conf = yaml.load(files)
    conf['Header'] = 'Monitoring'
    # parse start_vitrage
    conf['vitrage_conf_policy']['monitoring_tool'] = 'Zabbix'
    conf['vitrage_conf_policy']['server_ip'] = encoded_data['Zabbix_Server_IP']
    conf['vitrage_conf_policy']['server_port'] = encoded_data['Zabbix_Server_Port']
    conf['vitrage_conf_policy']['server_pass'] = encoded_data['Zabbix_Server_Password']
    conf['vitrage_conf_policy']['server_user'] = encoded_data['Zabbix_Server_User']

    if 'Host_IP' in encoded_data.keys():
        data = list()
        if ',' in encoded_data['Host_IP']:
            data = encoded_data['Host_IP'].split(',')
        else:
            data.append(encoded_data['Host_IP'])
        conf['vitrage_conf_policy']['vm_ip'] = data
        conf['app_monitoring_policy']['mgmt_ip'] = data

        data = list()
        if ',' in encoded_data['Host_ID']:
            data = encoded_data['Host_ID'].split(',')
        else:
            data.append(encoded_data['Host_ID'])
        conf['vitrage_conf_policy']['vm_id'] = data
        conf['vitrage_conf_policy']['vm_interface'] = encoded_data['Host_Interface_Name']
        conf['vitrage_conf_policy']['host_type'] = 'nova.host'

    else:
        data = list()
        if ',' in encoded_data['VM_IP']:
            data = encoded_data['VM_IP'].split(',')
        else:
            data.append(encoded_data['VM_IP'])
        conf['vitrage_conf_policy']['vm_ip'] = data
        conf['app_monitoring_policy']['mgmt_ip'] = data

        data = list()
        if ',' in encoded_data['VM_ID']:
            data = encoded_data['VM_ID'].split(',')
        else:
            data.append(encoded_data['VM_ID'])
        conf['vitrage_conf_policy']['vm_id'] = data
        conf['vitrage_conf_policy']['vm_interface'] = encoded_data['VM_Interface_Name']
        conf['vitrage_conf_policy']['host_type'] = 'nova.instance'

    data = list()
    if ',' in encoded_data['Zabbix_Host_Name']:
        data = encoded_data['Zabbix_Host_Name'].split(',')
    else:
        data.append(encoded_data['Zabbix_Host_Name'])
    conf['vitrage_conf_policy']['host_name'] = data
    conf['app_monitoring_policy']['host_name'] = data

    conf['vitrage_conf_policy']['host_type'] = encoded_data['Zabbix_Host_Type']

    #parse monitoring manager
    conf['app_monitoring_policy']['name'] = 'zabbix'
    conf['app_monitoring_policy']['zabbix_username'] = encoded_data['Zabbix_Server_User']
    conf['app_monitoring_policy']['zabbix_password'] = encoded_data['Zabbix_Server_Password']
    conf['app_monitoring_policy']['zabbix_server_ip'] = encoded_data['Zabbix_Server_IP']
    conf['app_monitoring_policy']['zabbix_server_port'] = encoded_data['Zabbix_Server_Port']


    conf['app_monitoring_policy']['parameters']['application']['app_name'] = encoded_data['App_name']
    conf['app_monitoring_policy']['parameters']['application']['app_port'] = encoded_data['App_port']
    conf['app_monitoring_policy']['parameters']['application']['ssh_username'] = encoded_data['Ssh_username']
    conf['app_monitoring_policy']['parameters']['application']['ssh_password'] = encoded_data['Ssh_password']

    if encoded_data['app_status'] == 'true':
        data = list()
        data.append(encoded_data['status_condition'])
        conf['app_monitoring_policy']['parameters']['application']['app_status']['condition'] = data
        # conf['app_monitoring_policy']['parameters']['application']['app_status']['cmd-action'] \
        #     = encoded_data['status_cmd']
    conf['app_monitoring_policy']['parameters']['application']['app_status']['usage'] = encoded_data['app_status']

    if encoded_data['app_memory'] == 'true':
        mem = encoded_data['memory_condition'].split(", ")
        value = int(mem[1])
        data = list()
        data.append(mem[0])
        data.append(value)
        conf['app_monitoring_policy']['parameters']['application']['app_memory']['condition'] = data
        # conf['app_monitoring_policy']['parameters']['application']['app_memory']['cmd-action'] \
        #     = encoded_data['memory_cmd']
    conf['app_monitoring_policy']['parameters']['application']['app_memory']['usage'] = encoded_data['app_memory']

    if encoded_data['agent_info'] == 'true':
        data = list()
        data.append(encoded_data['agentinfo_condition'])
        conf['app_monitoring_policy']['parameters']['OS']['os_agent_info']['condition'] = data
        # conf['app_monitoring_policy']['parameters']['OS']['os_agent_info']['cmd-action'] \
        #     = encoded_data['agent_cmd']
    conf['app_monitoring_policy']['parameters']['OS']['os_agent_info']['usage'] = encoded_data['agent_info']

    if encoded_data['proc_value'] == 'true':
        proc = encoded_data['procvalue_condition'].split(", ")
        value = int(proc[1])
        data = list()
        data.append(proc[0])
        data.append(value)    
        conf['app_monitoring_policy']['parameters']['OS']['os_proc_value']['condition'] = data
        # conf['app_monitoring_policy']['parameters']['OS']['os_proc_value']['cmd-action'] \
        #     = encoded_data['proc_cmd']
    conf['app_monitoring_policy']['parameters']['OS']['os_proc_value']['usage'] = encoded_data['proc_value']

    if encoded_data['cpu_load'] == 'true':
        load = encoded_data['cpuload_condition'].split(", ")
        value = int(load[1])
        data = list()
        data.append(load[0])
        data.append(value)
        conf['app_monitoring_policy']['parameters']['OS']['os_cpu_load']['condition'] = data
        # conf['app_monitoring_policy']['parameters']['OS']['os_cpu_load']['cmd-action'] \
        #     = encoded_data['cpu_load_cmd']
    conf['app_monitoring_policy']['parameters']['OS']['os_cpu_load']['usage'] = encoded_data['cpu_load']

    if encoded_data['cpu_usage'] == 'true':
        usage = encoded_data['cpuusage_condition'].split(", ")
        value = int(usage[1])
        data = list()
        data.append(usage[0])
        data.append(value)
        conf['app_monitoring_policy']['parameters']['OS']['os_cpu_usage']['condition'] = data
        # conf['app_monitoring_policy']['parameters']['OS']['os_cpu_usage']['cmd-action'] \
        #     = encoded_data['cpu_usage_cmd']
    conf['app_monitoring_policy']['parameters']['OS']['os_cpu_usage']['usage'] = encoded_data['cpu_usage']

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
