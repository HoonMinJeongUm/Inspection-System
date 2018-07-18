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
        print("")
        # listener.start_command(data[0], data[1], data[2])
        print(listener.start_command(['192.168.11.3', '192.168.11.31'], ['stack', 'stack'], 'ping -c 3 -q 192.168.11.1'))


