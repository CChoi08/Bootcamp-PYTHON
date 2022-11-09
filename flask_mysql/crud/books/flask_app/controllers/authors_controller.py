from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.author_model import Author
from flask_app.models.book_model import Book

@app.route('/')
def index():
    all_authors = Author.get_all()
    return render_template('authors.html', all_authors = all_authors)


@app.route('/authors/create', methods = ['POST'])
def author_create():
    data = {
        **request.form
    }
    Author.create(data)
    return redirect('/')


@app.route('/authors/<int:id>')
def author_by_id(id):
    data = {
        'id' : id
    }
    all_books = Book.select_some(data)
    one_author = Author.get_one_author(data)
    return render_template('author_fav.html', all_books = all_books, one_author = one_author)


@app.route('/authors/<int:id>/favorite', methods = ['POST'])
def add_fav_book(user_id):
    data = {
        'user_id' : user_id,
        'book_id' : request.form['book_id']
    }
    Author.create_favorite(data)
    return redirect(f'/authors/{data["user_id"]}')