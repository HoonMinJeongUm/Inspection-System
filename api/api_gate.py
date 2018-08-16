from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse, abort

import api_handler
import json
import ast
app = Flask(__name__)
api=Api(app)

@app.route('/Test',methods=['POST','PUT'])
def test_api():
	if not request.json:
		abort(400)
        data = request.json
        print(data)
        api_handler.start_action(data['action'],data)
   
	return ''

if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=5050,
            debug=True,)
