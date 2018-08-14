import api_arrange
import os
import sys
from check.case_manager import call_case
from test.case_manager import CaseManager
from monitoring.case_manager import MonitoringCaseManager
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
#from check.cases.base_controller import BaseController

# data = [['192.168.11.3', '192.168.11.31'],['root', 'root'],'netstat -nap | grep ESTAB | wc -l']
# call_case('Bottleneck',data)

def start_bottleneck(msg,ip1,ip2,mod1,mod2,test):
    sortdata = api_arrange.bottleneck(ip1,ip2,mod1,mod2,test)
    return call_case(msg,sortdata)

def start_monitoring_service(header,type,a,b,c,d,e,f,g,h,i,
                            k,l,m,n,o,
                            p,q,r,s,t,u,v,w,x,y,
                            z,a1,b1,c1,d1,e1,f1,g1,h1,i1,j1,k1):
    if header == 'vitrageconf':
        conf = api_arrange.monitoring_vitrageconf(header,type,a,b,c,d,e,f,g,h,i)
        print('#################################################')
        print(conf)
        print('#################################################')
        return 'test1'
    elif header=='manager':
        conf = api_arrange.monitoring_manager(header,type,
                                              k, l, m, n, o,
                                              p, q, r, s, t, u, v, w, x, y,
                                              z, a1, b1, c1, d1, e1, f1, g1, h1, i1, j1, k1)
        print('#################################################')
        print(conf)
        print('#################################################')
        return 'test2'


def start_test(case,tool,hosts,auth1,auth2,f_data1,f_data2,f_data3,f_data4,f_data5,f_data6):
    if case =='vnf':
        auth = api_arrange.test_auth(auth1,auth2)
        data_dic = api_arrange.test_vnf_dict(tool,f_data1,f_data2,f_data3,f_data4,f_data5,f_data6)
        print('#################################################')
        print(auth,data_dic)
        print('#################################################')
        return CaseManager.start(case=case,tool=tool,hosts=str(hosts),auth=auth,vnf_testing_args_dict=data_dic)
    elif case =='vim':
        requestdic = '{"NovaFlavors.create_flavor":[{"runner":{"type":"constant","concurrency":2,"times":10},"args":{"ram":500,"vcpus":1,"disk":1},"sla":{"failure_rate":{"max":0}}}]}'
        return CaseManager.start(case=case,tool=tool,requestdict=str(requestdic))