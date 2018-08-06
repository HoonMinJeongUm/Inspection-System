

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