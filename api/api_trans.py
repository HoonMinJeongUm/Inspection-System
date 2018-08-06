import json
import requests
import urllib
from flask import jsonify

url = "http://192.168.11.31:5000/api_gate/Bottleneck"

data = {'ip1':'192.168.11.3',
        'ip2':'192.168.11.31',
        'mod1':'root',
        'mod2':'root',
        'check':'Bottleneck',
        'test':'netstat -nap | grep ESTAB | wc -l'}

res = requests.post(url,data=json.dumps(data))

#
# params = json.dumps(data,indent=4).encode("utf-8")
# req = urllib.request(url,data=params,headers={'content-type':'application/json'})
# #req = urllib.request.Request(url,data=params,headers={'content-type':'application/json'})
# response = urllib.request.urlopen(req)
# print(response.read().decode('utf-8'))
# # data = [['192.168.11.3', '192.168.11.31'],['root', 'root'],'netstat -nap | grep ESTAB | wc -l']
# # call_case('Bottleneck',data)