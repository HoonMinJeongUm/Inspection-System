from check.cases.base_controller import BaseController

class Client(BaseController):
    def execute(self,data):
        print(data)