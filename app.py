from flask import Flask, request, render_template
from data_models import Author, Book
from base import db
import os

# Setting up flask-sqlalchemy with the database
file_path = os.path.abspath(os.getcwd())+"/data/library.db"
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+file_path

db.init_app(app)
with app.app_context():
    db.metadata.create_all(bind=db.engine)


@app.route("/add_author", methods=['GET', 'POST'])
def add_author():
    if request.method == 'GET':
        message = "Enter author's data"
        return render_template("authors_form.html", message=message)

    else:
        author = Author(
                        author_name=request.form.get("author", 'Default Author'),
                        author_birth_date=request.form.get("birth", "Default birth date"),
                        author_death_date=request.form.get("death", "Default death date")
                        )

        db.session.add(author)
        db.session.commit()
        message = "Author added, Want to add more?"
        return render_template("authors_form.html", message=message)


@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    if request.method == 'GET':
        message = "Enter book's data"
        authors = [author.author_name for author in Author.query.all()]
        return render_template("books.html", message=message, authors=authors)

    else:
        book = Book(
            book_name=request.form.get("book", 'Default Book'),
            book_author=request.form.get("author", 'Default Author'),
            book_isbn=request.form.get("ISBN", 1)
        )

        db.session.add(book)
        db.session.commit()
        message = "Book added, Want to add more?"
        return render_template("books.html", message=message)


@app.route("/", methods=["GET"])
def home():
    books = [book.book_name for book in Book.query.all()]
    return render_template("home.html", books=books)


@app.route("/<string:book>", methods=["GET"])
def book_info(book):
    book_data = Book.query.filter_by(book_name=book).all()
    return render_template("book.html", book_data=book_data[0])


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001)
