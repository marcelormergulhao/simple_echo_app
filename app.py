import os

from flask import Flask, request
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
    
class Echo(Resource):
    def get(self, message):
        return {'echo': f'{message}'}
    
class ComplexEcho(Resource):    
    def post(self):
        complex_message = request.form['data']
        return {'complexecho': f'{complex_message}'}
    
class EnvEcho(Resource):
    def get(self, env_key):
        value = os.environ.get(env_key)        
        return {'envecho': f'{value}'}

api.add_resource(HelloWorld, '/')
api.add_resource(Echo, '/echo/<string:message>')
api.add_resource(ComplexEcho, '/complexecho')
api.add_resource(EnvEcho, '/envecho/<string:env_key>')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")