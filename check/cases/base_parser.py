from abc import *
class BaseParser(metaclass=ABCMeta):
    @abstractmethod
    def parsing(self,result):
        pass

