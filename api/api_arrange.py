

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

def monitoring(tool, ip, port, pas, user, name, type, vm_ip, vm_id):
    dic_a = {'moitoring tool' :  str(tool),
             'servier_ip' : str(ip),
             'server_port' : str(port),
             'sever_pass' : str(pas),
             'server_user' : str(user),
             'host_name ' : str(name),
             'host_type' : str(type),
             'vm_ip' : str(vm_ip),
             'vm_id' : str(vm_id)}
    return dic_a