from models.author import AuthorModel
from flask import jsonify, request
from flask_restful import Resource, reqparse

class Authors(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'name',
        type = str,
        required = True,
        help = "This field cann't be blank!"
    )

    def post(self):

        data = Authors.parser.parse_args()
        author = AuthorModel.find_by_author_name(data['name'])

        if author:
            return{"message" : "{} already exists.".format(data['name'])}, 400

        author = AuthorModel(data['name'])
        try:
            author.save_to_db()
        except:
            {"message" : "Error occours."}, 404
        
        return author.json(), 201

class AuthorList(Resource):
    def get(self):
        authors = AuthorModel.query.all()
        return {"Author" : [author.json() for author in authors]}

class SearchAuthor(Resource):
    def get(self, author):
        author = AuthorModel.find_by_author_name(author)
        if author:
            return author.json()
        return {"message" : "Author not found"}, 404