from flask import Flask
from flask_restful import Resource, Api, reqparse
import api_handler
app = Flask(__name__)
api=Api(app)

class takeApi(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('service', type=str)
        parser.add_argument('request', type=str)
        args=parser.parse_args()

        service=args['service']
        request=args['request']

        api_handler.start(service, request)

        return

if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=5000,
            debug=True,)
