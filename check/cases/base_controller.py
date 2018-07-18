from abc import *
class BaseController(metaclass=ABCMeta):
    @abstractmethod
    def execute(self,data):
        pass
