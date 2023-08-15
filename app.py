from flask import Flask, request, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from data_models import Author, Book


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/library.db'

#Base = declarative_base()
#engine = create_engine("sqlite:///data/library.db")
#Session = sessionmaker(bind=engine)
#session = Session()

db = SQLAlchemy()
db.init_app(app)

#Base.metadata.create_all(engine)


@app.route("/add_author", methods=['GET', 'POST'])
def add_author():
    if request.method == 'GET':
        message = "Enter author's data"
        return render_template("authors_form.html", message=message)

    else:
        authors_data = request.form
        author = Author(
                        author_name=authors_data.get("name"),
                        author_birth_date=authors_data.get("author_birth_date"),
                        author_death_date=authors_data.get("author_death_date")
                        )

        db.session.add(author)
        db.session.commit()
        message = "Author added, Want to add more?"
        return render_template("authors_form.html", message=message)



@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    if request.method == 'GET':
        pass
    else:
        pass


@app.route("/home", methods=["GET"])
def home():
    return render_template("home.html")