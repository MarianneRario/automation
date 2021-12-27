from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()  # initialize
parser.add_argument('fb_link', required=True)
parser.add_argument('comment', required=True)
# args = parser.parse_args()  # parse arguments to dictionary
# data = pd.read_csv('activity.csv')

class MyApi(Resource):
    def __init__(self):
        self.__fbLink = parser.parse_args().get("fb_link", None)
        self.__comment = parser.parse_args().get("comment", None)

    def get(self):
        return {"Response": 200, "Data": parser.parse_args()}


api.add_resource(MyApi, '/activity/')  # add endpoints

if __name__ == '__main__':
    app.run()  # run our Flask app