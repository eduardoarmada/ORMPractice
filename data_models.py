from sqlalchemy import Column, String, Integer, ForeignKey, create_engine
from sqlalchemy.orm import mapped_column
from base import db


class Author(db.Model):
    __tablename__ = "authors"

    author_id = db.Column(db.Integer, primary_key=True)
    author_name = db.Column(db.String)
    author_birth_date = db.Column(db.String)
    author_death_date = db.Column(db.String)


class Book(db.Model):
    __tablename__ = "books"

    book_id = db.Column(db.Integer, primary_key=True)
    book_isbn = db.Column(db.Integer)
    book_name = db.Column(db.String)
    book_author = mapped_column(ForeignKey('authors.author_id'))
