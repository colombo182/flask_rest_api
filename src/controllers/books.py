import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property

from flask import Flask, jsonify, request

from flask_restplus import Api, Resource

from src.server.instance import server

app, api = server.app, server.api

books_db = [
    {'id': 0, 'title': 'War and Peace'},
    {'id': 1, 'title': 'Clean Code'}
]

@api.route('/books')
class Booklist(Resource):
    def get(self,):
        return books_db

    def post(self,):
        response = api.payload
        books_db.append(response)
        return response, 200