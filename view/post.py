from flask import request
from flask_restful import Resource

from flask_jwt_extended import get_jwt_identity, jwt_required

from controller.post import post_get, post, post_delete, post_update


class Post(Resource):
    @jwt_required()
    def post(self):
        title = request.json['title']
        content = request.json['content']
        user_id = get_jwt_identity()

        return post(
            title=title,
            content=content,
            user_id=user_id
        )


class GetPosts(Resource):
    @jwt_required()
    def get(self):
        return post_get()


class DeletePost(Resource):
    @jwt_required()
    def delete(self, id):
        token_Usr = get_jwt_identity()
        return post_delete(id=id,
                           token_Usr=token_Usr
                           )


class PutPost(Resource):
    @jwt_required()
    def put(self, id):
        title = request.json["title"]
        content = request.json["content"]
        token_Usr = get_jwt_identity()
        return post_update(
            id = id,
            title=title,
            content=content,
            token_Usr=token_Usr
        )