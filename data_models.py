from sqlalchemy import Column, String, Integer, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, mapped_column

Base = declarative_base()
engine = create_engine("sqlite:///data/library.db")


class Author(Base):
    __tablename__ = "authors"

    author_id = Column(Integer, primary_key=True)
    author_name = Column(String)
    author_birth_date = Column(String)
    author_death_date = Column(String)


class Book(Base):
    __tablename__ = "books"

    book_id = Column(Integer, primary_key=True)
    book_isbn = Column(Integer)
    book_name = Column(String)
    book_author = mapped_column(ForeignKey('authors.author_id'))


#Base.metadata.create_all(engine)
