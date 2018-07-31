from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse, abort
import api_handler
import json

app = Flask(__name__)
api=Api(app)

@app.route('/api_gate/<msg>',methods=['POST','PUT'])
def api_gate(msg):
    content = request.get_json(silent=True)
    print content
    return api_handler.start(content, msg)



# class CreateData(Resource):
#     def post(self, data1=None, data2=None):
#         parser = reqparse.RequestParser()
#         parser.add_argument('ip1', type=str)
#         parser.add_argument('ip2', type=str)
#         parser.add_argument('mod1', type=str)
#         parser.add_argument('mod2', type=str)
#         parser.add_argument('case', type=str)
#         parser.add_argument('test', type=str)
#         args = parser.parse_args()
#
#         _ip1 = args['ip1']
#         _ip2 = args['ip2']
#         _mod1 = args['mod1']
#         _mod2 = args['mod2']
#         _case = args['case']
#         _test = args['test']
#
#         data1[0] = _ip1
#         data1[1] = _ip2
#         data2[0] = _mod1
#         data2[1] = _mod2
#         data = data1 + data2 + _test
#         return jsonify(data)
#
# api.add_resource(CreateData,'/api_gate')
# @app.route('/api_gate',methods=['POST','PUT','GET'])
# def api_gate(data1=None, data2=None):
#     parser =reqparse.RequestParser()
#     parser.add_argument('ip1',type=str)
#     parser.add_argument('ip2',type=str)
#     parser.add_argument('mod1',type=str)
#     parser.add_argument('mod2',type=str)
#     parser.add_argument('case',type=str)
#     parser.add_argument('test',type=str)
#     args = parser.parse_args()
#
#     _ip1 = args['ip1']
#     _ip2 = args['ip2']
#     _mod1 = args['mod1']
#     _mod2 = args['mod2']
#     _case = args['case']
#     _test = args['test']
#
#     data1[0]=_ip1
#     data1[1]=_ip2
#     data2[0]=_mod1
#     data2[1]=_mod2
#     data = data1+data2+_test
#     return data

if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=5000,
            debug=True,)

# data = [['192.168.11.3', '192.168.11.31'],['root', 'root'],'netstat -nap | grep ESTAB | wc -l']
# call_case('Bottleneck',data)
# { "ip1" : "192.168.11.3", "ip2" : "192.168.11.31"