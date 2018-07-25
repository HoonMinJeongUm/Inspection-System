from check.cases.base_controller import BaseController
from ssh_manager import listener
from check.cases.p2p import parser

class Client(BaseController):
# ping -c 3 -q LOCAL IP(

    def __init__(self):
        self.pars = parser.P2PParser()

    def separate_data(self,info):
        print(info)
    def execute(self,data):
        # separate_data(data)
        # # ping -c 3 -q LOCAL IP(
        # we need to get DEST IP (Not HOSTs IP)
        print("Start Execute")
        hosts = data[0]
        auth = data[1]
        command = data[2]
        result = listener.start_command(hosts,auth,command)
        parsing_data = self.pars.parsing(hosts,command,result)

        print("===================================================================")
        print(parsing_data)
        print("===================================================================")
        return parsing_data

