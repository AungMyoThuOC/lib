from models.genre import GenreModel
from flask import jsonify, request
from flask_restful import Resource, reqparse

class Genre(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'name',
        type = str,
        required = True,
        help = "This field can't be blank!"
    )

    def post(self):

        data = Genre.parser.parse_args()
        author = GenreModel.find_by_genre_name(data['name'])

        if author:
            return {"message" : "{} already exists.".format(data['name'])}, 400

        author = GenreModel(data['name'])

        try:
            author.save_to_db()
        except:
            {"message" : "Error occours."}, 404

        return author.json(), 201

class GenreList(Resource):
    def get(self):
        genres = GenreModel.query.all()
        return {"Genre lsit" : [genre.json() for genre in genres]}

class SearchGenre(Resource):
    def get(self, genre):
        genre = GenreModel.find_by_genre_name(genre)

        if genre:
            return genre.json()
        return {"message" : "Genre not found"}, 404