#-*- coding: utf-8 -*-
# CASE MANAGER
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import subprocess, datetime, time, logging


logging.basicConfig(level=logging.DEBUG)
debug_logger = logging.getLogger(__name__)
debug_logger.setLevel(logging.DEBUG)

app = Flask(__name__)
api = Api(app)

# Todo - classify the requests

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=6005)