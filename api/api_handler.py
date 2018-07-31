import api_arrange
from check.cases.base_controller import BaseController

# data = [['192.168.11.3', '192.168.11.31'],['root', 'root'],'netstat -nap | grep ESTAB | wc -l']
# call_case('Bottleneck',data)

def start(content,msg):
    sortData=api_arrange.split(content)

    return call_case(msg,sortData)
