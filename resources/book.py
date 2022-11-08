from models.book import BookModel
from flask import Flask, jsonify, request
from flask_restful import Resource, reqparse

class Books(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'name',
        type = str,
        required = True,
        help = "This field is required"
    )

    parser.add_argument(
        'book_cover',
        type = str,
        required = False
    )

    parser.add_argument(
        'overview',
        type = str,
        required = True,
        help = "This field can't be blank!"
    )

    parser.add_argument(
        'publication_date',
        type = str,
        required = True,
        help = "This field can't be blank!"
    )

    parser.add_argument(
        'language',
        type = str,
        required = True,
        help = "This field can't be blank"
    )

    parser.add_argument(
        'b_id',
        type = str,
        required = False
    )

    parser.add_argument(
        'a_id',
        type = str,
        required = True,
        help = "Every book must have author id"
    )

    parser.add_argument(
        'g_id',
        type = str,
        required = True,
        help = "Every book must have genre id"
    )

    def post(self):
        
        data = Books.parser.parse_args()
        book = BookModel.find_by_book_name(data['name'])

        if book:
            return {"message" : "A book with tis name{} already exists.".format(data['name'])}, 400

        book = BookModel(data['name'], data['book_cover'], data['overview'], data['publication_date'], data['language'], data["a_id"], data["g_id"])

        try:
            book.save_to_db()
        except:
            return {"message" : "An error occoured while inserting data"}, 500

        return book.json(), 201

class SearchByBookName(Resource):
    def get(self, name):
        book = BookModel.find_by_book_name(name)

        if book:
            return book.json()
        return {"message" : "Item not found"}, 404

class BookList(Resource):
    def get(self):
        books = BookModel.query.all()
        return {"Books" : [book.json() for book in books]}

class SearchByLang(Resource):
    def get(self, lang):
        books = BookModel.find_by_language(lang)

        if books:
            return {"Books" : [book.json() for book in books]}

        return {"message" : "language not found"}, 404

class DeleteBook(Resource):
    def delete(self, b_id):
        book = BookModel.find_by_book_id(b_id)
        
        if book:
            book.delete_from_db()

        return {"message" : "Book delete successfully."}