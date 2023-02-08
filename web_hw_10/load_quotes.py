from xmlrpc.client import DateTime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Text, ForeignKey, ARRAY
import json

url_to_db = f'postgresql://postgres:123456@localhost:5432/postgres'

engine = create_engine(url_to_db, echo=True, pool_size=5)
DBSession = sessionmaker(bind=engine)
session = DBSession()

Base = declarative_base()

with open('authors.json', "r", encoding="utf8") as fh:
    unpacked_authors = json.load(fh)
    # print(unpacked_authors)

with open('quotes.json', "r", encoding="utf8") as fh:
    unpacked_quotes = json.load(fh)
    # print(unpacked_quotes)


# --------------------------------------------------------------------
class Authors_alchemy(Base):
    __tablename__ = 'app_quotes_authors'
    fullname = Column(primary_key=True)
    born_date = Column()
    born_location = Column()
    description = Column()


class Quotes_alchemy(Base):
    __tablename__ = 'app_quotes_quotes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    tags = Column(ARRAY(String))
    author_id = Column()
    quote = Column()


def upload_authors():
    for author in unpacked_authors:
        session.add(
            Authors_alchemy(
                fullname=author['fullname'],
                born_date=author['born_date'],
                born_location=author['born_location'],
                description=author['description']
            )
        )


def upload_quotes():
    for quote in unpacked_quotes:

        if quote['author'] == 'Alexandre Dumas fils':

            session.add(
                Quotes_alchemy(
                    tags=quote['tags'],
                    author_id='Alexandre Dumas-fils',
                    quote=quote['quote']

                )
            )

        else:
            session.add(
                Quotes_alchemy(
                    tags=quote['tags'],
                    author_id=quote['author'],
                    quote=quote['quote']

                )
            )


# --------------------------------------------------------------------
if __name__ == "__main__":
    # upload_authors()
    upload_quotes()
    session.commit()
