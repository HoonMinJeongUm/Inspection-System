import api_arrange
import os
import sys
from check.case_manager import call_case
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
#from check.cases.base_controller import BaseController

# data = [['192.168.11.3', '192.168.11.31'],['root', 'root'],'netstat -nap | grep ESTAB | wc -l']
# call_case('Bottleneck',data)

def start_bottleneck(msg,ip1,ip2,mod1,mod2,test):
    sortdata = api_arrange.bottleneck(ip1,ip2,mod1,mod2,test)
    return call_case(msg,sortdata)

def start_monitoring(tool,ip,port,pas,user,name,type,vm_ip,vm_id):
    sortdata = api_arrange.monitoring(tool,ip,port,pas,user,name,type,vm_ip,vm_id)
    print(sortdata)
    return "none"