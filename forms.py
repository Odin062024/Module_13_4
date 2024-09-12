from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class BookForm(FlaskForm):
    title = StringField('Tytuł', validators=[DataRequired()])
    isbn = StringField('ISBN')
    year_published = IntegerField('Rok wydania')
    submit = SubmitField('Dodaj książkę')

class BorrowForm(FlaskForm):
    borrower_name = StringField('Imię i nazwisko wypożyczającego', validators=[DataRequired()])
    submit = SubmitField('Wypożycz')
