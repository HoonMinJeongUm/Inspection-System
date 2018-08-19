import os
import sys
#import pickle
from api_arrange import monitoring_manager
from check import case_manager
from test.case_manager import CaseManager
from monitoring.case_manager import MonitoringCaseManager
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


def start_action(action,data):
	encoded_data = {k.encode(): v.encode() for k,v in data.iteritems()}
    	if action == 'Test':
		    vnf_testing_args_dict = None
		    requestdict = None
		    vnf_testing_args_dict = encoded_data

		    result = CaseManager.start(encoded_data['case'], encoded_data['tool'], encoded_data['host'], encoded_data['auth'], vnf_testing_args_dict, requestdict)
		    #print(result)
    	elif action == 'Check':
        	case_manager.call_case(encoded_data['case'],encoded_data)
    	elif action == 'Monitoring':
            data = monitoring_manager(encoded_data)
            MonitoringCaseManager(data)		   
