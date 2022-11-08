from this import d
from db import db

class GenreModel(db.Model):

    __tablename__ = "genre"

    id = db.Column(db.Integer, primary_key = True)
    genre = db.Column(db.String)

    books = db.relationship('BookModel', lazy = 'dynamic')

    def __init__(self, genre):
        self.genre = genre

    def json(self):
         return {'Genre id' : self.id, 'Genre' : self.genre, 'Books' : [book.json() for book in self.books.all()]}

    @classmethod
    def find_by_genre_name(cls, genre):
        return cls.query.filter_by(genre=genre).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()