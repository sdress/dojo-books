from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.author import Author
from flask_app.models.book import Book

@app.route('/')
def auto():
    return redirect('/authors')

@app.route('/authors')
def display_authors():
    return render_template('author_index.html', authors=Author.get_all())

@app.route('/authors/create', methods=['POST'])
def create_author():
    data = {'name': request.form['name']}
    Author.create(data)
    return redirect('/authors')

@app.route('/authors/<int:id>')
def show_author_favs(id):
    data = {'id': id}
    author = Author.get_one(data)
    favorite_books = Author.get_favorites(data)
    print(favorite_books)
    all_books = Book.get_all()
    return render_template('author_fav.html', author=author, favorites=favorite_books, books=all_books)