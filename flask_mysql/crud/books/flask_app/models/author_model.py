from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import book_model

class Author:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# ---------------------CLASSMETHODS---------------------------

    @classmethod
    def create(cls,data):
        query = '''
            INSERT INTO authors (name)
            VALUES (%(name)s);
        '''
        return connectToMySQL(DATABASE).query_db(query,data)


    @classmethod
    def get_all(cls):
        query = '''
            SELECT * FROM authors;
        '''
        results = connectToMySQL(DATABASE).query_db(query)
        author_instances = []
        if results:
            for row in results:
                this_author = cls(row)
                author_instances.append(this_author)
            return author_instances
        return []

# ---------------FAVORITES-----------------

    @classmethod
    def get_one_author(cls,data):
        query = '''
            SELECT * FROM authors
            LEFT JOIN favorites ON authors.id = favorites.author_id
            LEFT JOIN books ON books.id = favorites.book_id
            WHERE author.id = %(id)s;
        '''
        results = connectToMySQL(DATABASE).query_db(query,data)

        if results:
            books_list = []
            this_author = cls(results[0])
            for row in results:
                book_data = {
                    **row,
                    'id' : row['books.id'],
                    'created_at' : row['books.created_at'],
                    'updated_at' : row['books.updated_at']
                }
                this_book_instance = book_model.Book(book_data)
                books_list.append(this_book_instance)
            this_author.books = books_list
            return this_author
        return False


    @classmethod
    def create_favorite(cls,data):
        query = '''
            INSERT INTO favorites (user_id, book_id)
            VALUES (%(user_id)s, %(book_id)s)
        '''
        return connectToMySQL(DATABASE).query_db(query,data)


    @classmethod
    def select_some(cls,data):
        query = '''
            SELECT * FROM authors
            WHERE authors.id NOT IN
            (SELECT user_id FROM favorites WHERE book_id = %(id)s)
        '''
        results = connectToMySQL(DATABASE).query_db(query,data)
        authors_list = []

        if results:
            for row in results:
                authors_list.append(cls(row))
            return authors_list
        return []