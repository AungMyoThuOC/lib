from db import db

class BookModel(db.Model):

    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    book_cover = db.Column(db.String)
    overview = db.Column(db.String)
    publication_date = db.Column(db.String)
    language = db.Column(db.String)

    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))
    author = db.relationship('AuthorModel')

    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))
    genre = db.relationship("GenreModel")

    def __init__(self, name, book_cover, overview, publication_date, language, author_id, genre_id):
        self.name = name
        self.book_cover = book_cover
        self.overview = overview
        self.publication_date = publication_date
        self.language = language

        self.author_id = author_id
        self.genre_id = genre_id

    def json(self):
        return {'book id' : self.id,'name' : self.name, 'book_cover' : self.book_cover, 'overview' : self.overview, 'publication_date' : self.publication_date, 'language' : self.language, 'author_id' : self.author_id, 'genre_id' : self.genre_id}

    @classmethod
    def find_by_book_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_book_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_language(cls, language):
        return cls.query.filter_by(language=language).all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()