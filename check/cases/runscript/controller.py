from check.cases.base_controller import BaseController
from ssh_manager import listener
from check.cases.runscript import parser

class Client(BaseController):

    def __init__(self):
        self.pars = parser.P2PParser()

    def separate_data(self,info):
        print(data)

    def execute(self, data):
        # separate_data(data)
        print("Start Execute")
        """We need to sperate parameter at data"""
        hosts = data[0]
        auth = data[1]
        local_script = data[2]
        remote_script = data[3]
        file_name = "test_script"
        result = listener.start_script(hosts, auth, file_name,local_script,remote_script)
        print("===================================================================")
        print(result)
        print("===================================================================")