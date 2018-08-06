import api_arrange
import os
import sys
from check.case_manager import call_case
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
#from check.cases.base_controller import BaseController

# data = [['192.168.11.3', '192.168.11.31'],['root', 'root'],'netstat -nap | grep ESTAB | wc -l']
# call_case('Bottleneck',data)

def start(msg,ip1,ip2,mod1,mod2,test):
    if msg == 'Bottleneck':
        sortdata = api_arrange.bottleneck(ip1,ip2,mod1,mod2,test)
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print(sortdata)
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    else :
        sortdata = "none"

    return call_case(msg,sortdata)
