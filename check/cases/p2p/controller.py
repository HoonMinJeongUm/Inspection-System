from check.cases.base_controller import BaseController
from ssh_manager import listener

class Client(BaseController):
# ping -c 3 -q LOCAL IP(

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
        print("===================================================================")
        print(result)
        print("===================================================================")

    # start_command(['192.168.11.3','192.168.11.31'],['stack','stack'],'uname -a') <= TEST Line

