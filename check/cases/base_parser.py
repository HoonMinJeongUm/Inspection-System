from abc import *
class BaseParser(metaclass=ABCMeta):

    @abstractmethod
    def parsing(self,hosts,command,result):
        pass

