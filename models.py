from app import db
from datetime import datetime

# Relacja wiele-do-wielu między książką a autorem
book_author = db.Table('book_author',
    db.Column('book_id', db.Integer, db.ForeignKey('book.id')),
    db.Column('author_id', db.Integer, db.ForeignKey('author.id'))
)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    isbn = db.Column(db.String(13), nullable=True)
    year_published = db.Column(db.Integer, nullable=True)
    on_shelf = db.Column(db.Boolean, default=True)
    authors = db.relationship('Author', secondary=book_author, backref=db.backref('books', lazy='dynamic'))

    def __repr__(self):
        return f"<Book {self.title}>"

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        return f"<Author {self.first_name} {self.last_name}>"

class Borrow(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    borrower_name = db.Column(db.String(128), nullable=False)
    borrow_date = db.Column(db.DateTime, default=datetime.utcnow)
    return_date = db.Column(db.DateTime, nullable=True)

    book = db.relationship('Book', backref='borrows')

    def __repr__(self):
        return f"<Borrow {self.borrower_name} borrowed {self.book.title}>"
