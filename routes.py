from flask import render_template, redirect, url_for, flash
from app import app, db
from models import Book, Author, Borrow
from forms import BookForm, BorrowForm

@app.route('/')
def book_list():
    books = Book.query.all()
    return render_template('book_list.html', books=books)

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    form = BookForm()
    if form.validate_on_submit():
        new_book = Book(title=form.title.data, isbn=form.isbn.data, year_published=form.year_published.data)
        db.session.add(new_book)
        db.session.commit()
        flash('Książka została dodana!')
        return redirect(url_for('book_list'))
    return render_template('add_book.html', form=form)

@app.route('/borrow/<int:book_id>', methods=['GET', 'POST'])
def borrow_book(book_id):
    book = Book.query.get_or_404(book_id)
    form = BorrowForm()
    if form.validate_on_submit():
        if not book.on_shelf:
            flash('Książka jest już wypożyczona.')
            return redirect(url_for('book_list'))
        
        borrow = Borrow(book_id=book.id, borrower_name=form.borrower_name.data)
        book.on_shelf = False
        db.session.add(borrow)
        db.session.commit()
        flash(f'Książka "{book.title}" została wypożyczona!')
        return redirect(url_for('book_list'))
    return render_template('borrow_book.html', form=form, book=book)
