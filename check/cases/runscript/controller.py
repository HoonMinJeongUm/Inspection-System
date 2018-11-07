from check.cases.base_controller import BaseController
from ssh_manager import listener
from check.cases.runscript import parser

class Client():

    def __init__(self):
        pass

    def separate_data(self,info):
        print(data)

    def execute(self, data):
        # separate_data(data)
        print("Start Execute")
        print("DATA",data)
        hosts = []
        hosts.append('192.168.11.11')
        auth = ['root','root']
        local_script = '/opt/stack'
        remote_script = '/opt/stack/path'
        file_name = "cpu.sh"
        result = listener.start_script(hosts, auth, file_name,local_script,remote_script)
        print("===================================================================")
        print(result)
        print("===================================================================")
