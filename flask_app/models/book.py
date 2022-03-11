from flask_app.config.mysqlconnection import connectToMySQL

db = 'books_schema'

class Book:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    # create
    @classmethod
    def create(cls, data):
        query = "INSERT INTO books (title, num_of_pages, created_at, updated_at) VALUES ( %(title)s, %(num_of_pages)s, NOW(), NOW() );"
        return connectToMySQL(db).query_db(query, data)

    # read
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL(db).query_db(query)
        all_books = []
        for book in results:
            all_books.append( cls(book) )
        return all_books
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM books WHERE id = %(id)s;"
        results = connectToMySQL(db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    # update
    @classmethod
    def update(cls, data):
        query = "UPDATE books SET title = %(title)s, num_of_pages = %(num_of_pages)s WHERE id = %(id)s;"
        return connectToMySQL(db).query_db(query, data)
    
    # delete
    def delete(cls, data):
        query = "DELETE * FROM books WHERE id = %(id)s;"
        return connectToMySQL(db).query_db(query, data)