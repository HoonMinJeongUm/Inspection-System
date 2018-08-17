from check.cases.base_controller import BaseController
from ssh_manager import listener
from check.cases.p2p import parser

class Client():
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
        

        hosts = []
        if ',' in data['Hosts'] :
            hosts = data['Hosts'].split(',')
        else: 
            hosts.append(data['Hosts'])
        auth = [data['SSH_ID'],data['SSH_PWD']]
        command = 'ping -c 3 -q localhost'
        print(hosts)
        print(auth)
        print(command)
        result = listener.start_command(hosts,auth,command)
        parsing_data = self.pars.parsing(hosts,command,result)

        print("===================================================================")
        print(parsing_data)
        print("===================================================================")
        return parsing_data

