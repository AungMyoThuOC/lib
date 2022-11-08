from multiprocessing import connection
import sqlite3

connection = sqlite3.connect("library.db")

cursor = connection.cursor()

create_user_table = "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, password text, role int)"
cursor.execute(create_user_table)

create_genre_table = "CREATE TABLE IF NOT EXISTS genre(id INTEGER PRIMARY KEY, genre text)"
cursor.execute(create_genre_table)

create_author_table = "CREATE TABLE IF NOT EXISTS authors(id INTEGER PRIMARY KEY, author text)"
cursor.execute(create_author_table)

create_book_table = "CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY, name text, book_cover text, overview text, publication_date text, language text)"
cursor.execute(create_book_table)

connection.commit()
connection.close()