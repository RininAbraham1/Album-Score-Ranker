from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite database
engine = create_engine("sqlite:///albums.db", echo=False)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# Album table (optional, could just use ratings table)
class Album(Base):
    __tablename__ = "albums"
    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True)
    artist = Column(String)

# Ratings table
class Rating(Base):
    __tablename__ = "ratings"
    id = Column(Integer, primary_key=True)
    album_title = Column(String)
    rating = Column(Float)

# Create tables
Base.metadata.create_all(engine)

