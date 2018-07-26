from check.cases.base_parser import BaseParser

class P2PParser(BaseParser):
    def __init__(self):
        pass

    def parsing(self,hosts,command,result):
        """
        We need to add some code for chaged result
        """
        parsing_data = result
        parsing_result = ''

        for host in hosts:
            start_slicing = parsing_data.find('['+host+'] out: ---')
            end_slicing = parsing_data.find(' ms\n['+host+']')
            parsing_result += (parsing_data[start_slicing:end_slicing] + ' ms\n')
        return parsing_data
