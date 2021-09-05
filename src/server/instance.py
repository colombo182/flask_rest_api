import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property

from flask import Flask, jsonify, request

from flask_restplus import Api

class Server():
    def __init__(self,):
        self.app = Flask(__name__)
        self.api = Api(
            self.app,
            version ='1.0',
            title = 'Sample Book API',
            description = 'A simple book API',
            doc = '/docs'
        )

    def run(self,):
        self.app.run(
            debug = True
    )

server = Server()