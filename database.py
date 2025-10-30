from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()
engine = create_engine("sqlite:///sample_albums.db", echo=False)
Session = sessionmaker(bind=engine)
session = Session()

class Album(Base):
    __tablename__ = "albums"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    artist = Column(String)
    score = Column(Float)

def get_all_albums():
    albums = session.query(Album).all()
    return [{"title": a.title, "artist": a.artist, "score": a.score} for a in albums]

def add_rating(title, rating):
    album = session.query(Album).filter_by(title=title).first()
    if album:
        # Simple example: update average
        album.score = (album.score + rating) / 2
        session.commit()
        return True
    return False

if __name__ == "__main__":
    Base.metadata.create_all(engine)
