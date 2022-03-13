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
    return render_template('author_fav.html', author=Author.get_one(data), favorites=Author.get_favorites(data), books=Book.get_all())

@app.route('/authors/<int:id>/add', methods = ['POST'])
def add_fav_book(id):
    data = {
        'author_id': id,
        'book_id': request.form['title']
    }
    Author.add_favorite(data)
    return redirect(f'/authors/{id}')