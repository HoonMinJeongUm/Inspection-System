import json

def split(contnet):
    dict = json.loads(contnet)
    a = [dict['ip1'],dict['ip2']]
    b = [dict['mod1'],dict['mod2']]
    c = dict['test']
    d = [a,b,c]
    return d