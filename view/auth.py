from flask import request
from flask_restful import Resource
from controller.auth import sigup, auth, login


class SigUp(Resource):
    def post(self):
        id = request.json['id']
        name = request.json['name']
        password = request.json['password']

        return sigup(
                id=id,
                name=name,
                password=password
                     )


class Auth(Resource):
    def post(self):
        id = request.json["id"]

        return auth(
            id=id
        )


class Login(Resource):
    def post(self):
        id = request.json['id']
        password = request.json['password']

        return login(
            id=id,
            password=password
        )