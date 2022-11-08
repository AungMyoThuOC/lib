from flask import Flask
from flask_restful import Api
#from flask_jwt_extended import JWTManager
from db import db
from security import authenticate, identity
from resources.author import Authors, AuthorList, SearchAuthor
from resources.book import Books, BookList, SearchByLang, SearchByBookName, DeleteBook
from resources.genre import Genre, GenreList, SearchGenre
from resources.user import UserRegister, UserList, User

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///library.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)
app.secret_key = "onii-chan yemete"

api.add_resource(Authors, '/author/add')
api.add_resource(AuthorList, '/authors/all')
api.add_resource(SearchAuthor, '/author/<string:author>')

api.add_resource(Books, '/book/add')
api.add_resource(BookList, '/books')
# api.add_resource(SearchByLang, 'books/lang/<string:lang>')
api.add_resource(SearchByBookName, '/books/<string:name>')
api.add_resource(DeleteBook, '/book/delete/<int:b_id>')

api.add_resource(Genre, '/genre/add')
api.add_resource(GenreList, '/genre/all')
api.add_resource(SearchGenre, '/genre/<string:genre>')

api.add_resource(UserRegister, '/register')
api.add_resource(UserList, '/alluser')
api.add_resource(User, '/user/<int:uid>')

@app.before_first_request
def create_table():
    db.create_all()


if __name__ == "__main__":

    from db import db
    db.init_app(app)

    app.run(port=5000 ,debug=True, host='0.0.0.0')