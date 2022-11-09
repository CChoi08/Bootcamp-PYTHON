from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import author_model

class Book:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# ---------------------CLASSMETHODS---------------------------

    @classmethod
    def create(cls,data):
        query = '''
            INSERT INTO books (title, num_of_pages)
            VALUES (%(title)s, %(num_of_pages)s);
        '''
        return connectToMySQL(DATABASE).query_db(query,data)


    @classmethod
    def get_all(cls):
        query = '''
            SELECT * FROM books;
        '''
        results = connectToMySQL(DATABASE).query_db(query)
        book_instances = []
        if results:
            for row in results:
                this_book = cls(row)
                book_instances.append(this_book)
            return book_instances
        return []

# ---------------FAVORITES-----------------

    @classmethod
    def get_one_book(cls,data):
        query = '''
            SELECT * FROM books
            LEFT JOIN favorites ON books.id = favorites.book_id
            LEFT JOIN users ON authors.id = favorits.author_id
            WHERE books.id = %(id)s;
        '''
        results = connectToMySQL(DATABASE).query_db(query,data)

        if results:
            authors_list = []
            this_book = cls(results[0])
            for row in results:
                author_data = {
                    **row,
                    'created_at' : row['created_at'],
                    'updated_at' : row['updated_at']
                }
                this_author_instance = author_model.Author(author_data)
                authors_list.append(this_author_instance)
            this_book.books = authors_list
            return this_book
        return False


    @classmethod
    def select_some(cls,data):
        query = '''
            SELECT * FROM books
            WHERE books.id NOT IN
            (SELECT book_id FROM favorites WHERE author_id = %(id)s)
        '''
        results = connectToMySQL(DATABASE).query_db(query,data)
        books_list = []

        if results:
            for row in results:
                books_list.append(cls(row))
            return books_list
        return []

