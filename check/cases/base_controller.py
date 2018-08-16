import abc
class BaseController(abc.ABCMeta):
    def __init__(self):
        pass
    @abc.abstractmethod
    def execute(self,data):
        pass

    @abc.abstractmethod
    def separate_data(self,info):
        pass
