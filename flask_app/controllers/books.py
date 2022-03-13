from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.author import Author
from flask_app.models.book import Book

@app.route('/books')
def display_books():
    books = Book.get_all()
    print(books)
    return render_template('book_index.html', books=books)

@app.route('/books/create', methods = ['POST'])
def create_book():
    data = {
        'title': request.form['title'],
        'num_of_pages': request.form['num_of_pages']
    }
    Book.create(data)
    return redirect('/books')

@app.route('/books/<int:id>')
def show_book_favs(id):
    data = {'id': id}
    return render_template('book_fav.html', book = Book.get_one(data), authors = Author.get_all(), favorites = Book.get_favorites(data))

@app.route('/books/<int:id>/add', methods = ['POST'])
def add_fav_author(id):
    data = {
        'book_id': id,
        'author_id': request.form['name'],
    }
    Book.add_favorite(data)
    return redirect(f'/books/{id}')