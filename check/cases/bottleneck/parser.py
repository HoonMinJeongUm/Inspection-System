from check.cases.base_parser import BaseParser

class BottleneckParser():
    def __init__(self):
        pass

    def parsing(self,hosts,command,result):
        """
        We need to add some code for chaged result
        """
        parsing_data = result
        parsing_result = ''

        for host in hosts:
            start_slicing = parsing_data.find('['+host+'] run: ' + command)
            end_slicing = parsing_data.find('['+host+'] out: \n\n')
            parsing_result += (parsing_data[start_slicing:end_slicing].rstrip('\n') + ' number\n')
        return parsing_result
