from check.cases.base_controller import BaseController
from ssh_manager import listener
from check.cases.bottleneck import parser

class Client():

    def __init__(self):
        self.pars = parser.BottleneckParser()


    def separate_data(self,info):
        print(data)

    def execute(self,data):
        # separate_data(data)
        # netstat - nap | grep ESTAB | wc - l
        # netstat - nap | grep:80 | grep ESTAB | wc - l

        # separate_data(data)
        # Two case L 1. netstat - nap | grep ESTAB | wc -l
        #            2. netstat - nap | <custom port> | grep ESTAB | wc -l

        print("Start Execute")

        hosts = []
        #if ',' in data['Hosts'] :
        #    hosts = data['Hosts'].split(',')
        #else:
        #    hosts.insert( data['Hosts'])
        auth = [data['SSH_ID'],data['SSH_PWD']]
        port = data['Port']
        hosts = ['127.0.0.1']
        command = 'netstat - nap | ' + port + ' |  grep ESTAB | wc -l'
        print(hosts)
        print(auth)
        print(command)

        result = listener.start_command(hosts, auth, command)
        parsing_data = self.pars.parsing(hosts,command,result)

        print("===================================================================")
        print(parsing_data)
        print("=================================================================")
        return parsing_data
