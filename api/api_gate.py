from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse, abort
import api_handler
import json

app = Flask(__name__)
api=Api(app)

@app.route('/api_gate/Bottleneck/<ip1>/<ip2>/<mod1>/<mod2>/<test>',methods=['POST','PUT'])
def api_bottleneck(ip1,ip2,mod1,mod2,test):
    return api_handler.start_bottleneck('Bottleneck',ip1,ip2,mod1,mod2,test)

@app.route('/api_gate/Monitoring/<header>/<type>/<a>/<b>/<c>/<d>/<e>/<f>/<g>/<h>/<i>/<k>/<l>/<m>/<n>/<o>/<p>/<q>/<r>/<s>/<t>/<u>/<v>/<w>/<x>/<y>/<z>/<a1>/<b1>/<c1>/<d1>/<e1>/<f1>/<g1>/<h1>/<i1>/<j1>/<k1>',methods=['POST','PUT'])
def api_monitoring_initiate(header,type,a,b,c,d,e,f,g,h,i,
                            k,l,m,n,o,
                            p,q,r,s,t,u,v,w,x,y,
                            z,a1,b1,c1,d1,e1,f1,g1,h1,i1,j1,k1):
    return api_handler.start_monitoring_service(header,type,a,b,c,d,e,f,g,h,i,
                            k,l,m,n,o,
                            p,q,r,s,t,u,v,w,x,y,
                            z,a1,b1,c1,d1,e1,f1,g1,h1,i1,j1,k1)

@app.route('/api_gate/Test/<case>/<tool>/<hosts>/<auth1>/<auth2>/<f_data1>/<f_data2>/<f_data3>/<f_data4>/<f_data5>/<f_data6>',methods=['POST','PUT'])
def apI_test(case,tool,hosts,auth1,auth2,f_data1,f_data2,f_data3,f_data4,f_data5,f_data6):
    return api_handler.start_test(case,tool,hosts,auth1,auth2,f_data1,f_data2,f_data3,f_data4,f_data5,f_data6)


if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=5000,
            debug=True,)
