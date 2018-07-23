from check.cases.base_controller import BaseController
from ssh_manager import listener
from check.cases.bottleneck import parser

class Client(BaseController):

    def __init__(self):
        self.pars = parser.P2PParser()


    def separate_data(self,info):
        print(data)

    def execute(self,data):
        # separate_data(data)
        print(data)
        # netstat - nap | grep ESTAB | wc - l <= 단어수를 새준다(모든 서비스 동시 접속자수)
        # netstat - nap | grep:80 | grep ESTAB | wc - l(웹 동시접속자 수)

        # separate_data(data)
        # Two case L 1. netstat - nap | grep ESTAB | wc -l
        #            2. netstat - nap | <custom port> | grep ESTAB | wc -l

        print("Start Execute")
        hosts = data[0]
        auth = data[1]
        command = data[2]
        result = listener.start_command(hosts, auth, command)
        print("===================================================================")
        print(result)
        print("===================================================================")

        # start_command(['192.168.11.3','192.168.11.31'],['stack','stack'],'uname -a')P <= TEST Line
