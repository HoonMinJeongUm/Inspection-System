from check.cases.base_controller import BaseController

class Client(BaseController):
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