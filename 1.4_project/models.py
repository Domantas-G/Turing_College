from sqlalchemy import (
    Boolean,
    BigInteger,
    Column,
    create_engine,
    Float,
    ForeignKey,
    Integer,
    PrimaryKeyConstraint,
    String,
    text,
)
from sqlalchemy.orm import relationship
from database import Base


class Titles(Base):
    __tablename__ = "titles"

    id = Column(String(20), primary_key=True)
    title = Column(String(300), nullable=False)
    release_year = Column(Integer)
    age_certification = Column(String(10))
    runtime = Column(Integer)
    imdb_id = Column(String(20))
    imdb_score = Column(Float)
    imdb_votes = Column(Integer)
    is_best_movie_by_year = Column(Boolean)
    is_best_movie = Column(Boolean)
    is_best_show_by_year = Column(Boolean)
    is_best_show = Column(Boolean)

    title_type = relationship("TitleType", uselist=False, back_populates="titles")
    title_genres = relationship("TitleGenres", back_populates="titles")
    title_production_countries = relationship(
        "TitleProductionCountries", back_populates="titles"
    )
    credits = relationship("Credits", back_populates="titles")


class TitleType(Base):
    __tablename__ = "title_type"

    type_id = Column(Integer, autoincrement=True)
    id = Column(String(20), ForeignKey("titles.id"))
    type = Column(String(50))

    __table_args__ = (PrimaryKeyConstraint("type_id", "id"),)

    titles = relationship("Titles", back_populates="title_type")


class TitleGenres(Base):
    __tablename__ = "title_genres"

    genre_id = Column(Integer, autoincrement=True)
    id = Column(String(20), ForeignKey("titles.id"))
    genre = Column(String(50))

    __table_args__ = (PrimaryKeyConstraint("genre_id", "id"),)

    titles = relationship("Titles", back_populates="title_genres")


class TitleProductionCountries(Base):
    __tablename__ = "title_production_countries"

    production_id = Column(Integer, autoincrement=True)
    id = Column(String(20), ForeignKey("titles.id"))
    country = Column(String(50))

    __table_args__ = (PrimaryKeyConstraint("production_id", "id"),)

    titles = relationship("Titles", back_populates="title_production_countries")


class Persons(Base):
    __tablename__ = "persons"

    person_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(300), nullable=False)

    credits = relationship("Credits", back_populates="persons")


class Credits(Base):
    __tablename__ = "credits"

    credit_id = Column(Integer, primary_key=True, autoincrement=True)
    id = Column(String(20), ForeignKey("titles.id"))
    person_id = Column(Integer, ForeignKey("persons.person_id"))
    character = Column(String(300))
    role = Column(String(50))

    titles = relationship("Titles", back_populates="credits")
    persons = relationship("Persons", back_populates="credits")
