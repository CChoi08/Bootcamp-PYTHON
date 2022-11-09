from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.book_model import Book
from flask_app.models.author_model import Author

@app.route('/books/new')
def books_page():
    all_books = Book.get_all()
    return render_template('books.html', all_books = all_books)

@app.route('/books/create', methods = ['POST'])
def book_create():
    data = {
        **request.form
    }
    Book.create(data)
    return redirect('/books/new')


@app.route('/books/<int:id>')
def show_book(id):
    data = {
        'id' : id
    }
    all_authors = Book.get_one_book(data)
    some_authors = Author.select_some(data)
    return render_template('book_favorite.html', all_authors = all_authors, some_authors = some_authors)


@app.route('/books/<int:book_id>/favorite', methods = ['POST'])
def add_fav_author(book_id):
    data = {
        'book_id' : book_id,
        'user_id' : request.form['user_id']
    }
    Author.create_favorite(data)
    return redirect(f'/books/{data["books_id"]}')