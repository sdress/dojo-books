from flask_app.config.mysqlconnection import connectToMySQL

db = 'books_schema'

class Author:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    # create
    @classmethod
    def create(cls, data):
        query = "INSERT INTO authors (name, created_at, updated_at) VALUES ( %(name)s, NOW(), NOW() );"
        return connectToMySQL(db).query_db(query, data)
    
    @classmethod
    def add_favorite(cls, data):
        pass

    # read
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL(db).query_db(query)
        all_authors = []
        for author in results:
            all_authors.append( cls(author) )
        return all_authors
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM authors WHERE id = %(id)s;"
        results = connectToMySQL(db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])
    
    @classmethod
    def get_favorites(cls, data):
        query = "SELECT * FROM authors LEFT JOIN favorites ON favorites.author_id = authors.id LEFT JOIN books ON favorites.book_id = books.id WHERE authors.id= %(id)s;"
        results = connectToMySQL(db).query_db(query, data)
        fav_books = []
        if len(results) < 1:
            return False
        for book in results:
            fav_books.append( cls(book) )
        return fav_books

    # update
    @classmethod
    def update(cls, data):
        query = "UPDATE authors SET name = %(name)s WHERE id = %(id)s;"
        return connectToMySQL(db).query_db(query, data)
    
    # delete
    def delete(cls, data):
        query = "DELETE * FROM authors WHERE id = %(id)s;"
        return connectToMySQL(db).query_db(query, data)