from fastapi import FastAPI, HTTPException, Depends, status

# from pydantic import BaseModel, Field, BaseSettings, constr, conint, confloat, validator
from typing import Optional, Annotated

from database import engine, SessionLocal
import models
from sqlalchemy.orm import Session

app = FastAPI()

# To create databade tables
# models.Base.metadata.create_all(bind=engine)

# To run:
# uvicorn db_api:app --reload
# http://127.0.0.1:8000/docs


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@app.get("/")
def read_something():
    return {"msg": "something"}


# class DatabaseSettings(BaseSettings):
#     DATABASE_DRIVER: str
#     DATABASE_USERNAME: str
#     DATABASE_PASSWORD: str
#     DATABASE_HOST: str
#     DATABASE_PORT: int
#     DATABASE_NAME: str

#     class Config:
#         # Takes info from settings.env
#         env_file = ".env"


# settings = DatabaseSettings()

# database_url = f"{settings.DATABASE_DRIVER}://{settings.DATABASE_USERNAME}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_HOST}:{settings.DATABASE_PORT}/{settings.DATABASE_NAME}"


# # Titles Model
# class TitleModel(BaseModel):
#     id: constr(max_length=20)  # Or str = Field(min_length=1,  max_length=20)
#     title: constr(max_length=300)
#     release_year: conint(gt=1800)
#     age_certification: Optional[constr(max_length=10)] = None
#     runtime: conint(ge=0)
#     imdb_id: Optional[constr(max_length=20)] = None
#     imdb_score: confloat(ge=0)
#     imdb_votes: conint(ge=0)
#     is_best_movie_by_year: bool
#     is_best_movie: bool
#     is_best_show_by_year: bool
#     is_best_show: bool

#     # @validator('id')
#     # def validate_id_length(cls, value):
#     #     if len(value)=0 :
#     #         raise ValueError('id length must be >0')
#     #     return value

#     # For some list to be split and returned value before Validators take place.
#     # @validator('some_list', pre=True)
#     # def split_list(cls, value):
#     #     return value.split(",")

#     class Config:
#         use_enum_values = True
#         title = "Some Title"
#         extra = "allow"
#         # This will strip any whitespace in all fields
#         anystr_strip_whitespace = True


# # TitleType Model
# class TitleTypeModel(BaseModel):
#     type_id: conint(gt=0)
#     id: constr(max_length=20)
#     type: constr(max_length=50)


# # TitleGenres Model
# class TitleGenresModel(BaseModel):
#     genre_id: conint(ge=0)
#     id: constr(max_length=20)
#     genre: Optional[constr(max_length=50)] = None


# # TitleProductionCountries Model
# class TitleProductionCountriesModel(BaseModel):
#     production_id: conint(ge=0)
#     id: constr(max_length=20)
#     country: Optional[constr(max_length=50)] = None


# # Persons Model
# class PersonsModel(BaseModel):
#     person_id: conint(ge=0)
#     name: constr(max_length=300)


# # Credits Model
# class CreditsModel(BaseModel):
#     credit_id: conint(ge=0)
#     id: constr(max_length=20)
#     person_id: conint(ge=0)
#     character: Optional[constr(max_length=300)] = None
#     role: constr(max_length=50)


# # def main() -> None:

# # Read data from a JSON file
# # with open("./data.json") as file:
# #     data = json.load(file)
# #     books: List[Book] = [Book(**item) for item in data]
# #     # print(books)
# #     print(books[0])
# # print(books[0].dict(exclude={"price"}))
# # print(books[1].copy())


# # if __name__ == "__main__":
# # main()


# # # Titles Model
# # class TitleModel(BaseModel):
# #     id: str
# #     title: str
# #     release_year: int
# #     age_certification: Optional[str] = None
# #     runtime: int
# #     imdb_id: Optional[str] = None
# #     imdb_score: float
# #     imdb_votes: int
# #     is_best_movie_by_year: bool
# #     is_best_movie: bool
# #     is_best_show_by_year: bool
# #     is_best_show: bool


# # # TitleType Model
# # class TitleTypeModel(BaseModel):
# #     type_id: int
# #     id: str
# #     type: str


# # # TitleGenres Model
# # class TitleGenresModel(BaseModel):
# #     genre_id: int
# #     id: str
# #     genre: Optional[str] = None


# # # TitleProductionCountries Model
# # class TitleProductionCountriesModel(BaseModel):
# #     production_id: int
# #     id: str
# #     country: Optional[str] = None


# # # Persons Model
# # class PersonsModel(BaseModel):
# #     person_id: int
# #     name: str


# # # Credits Model
# # class CreditsModel(BaseModel):
# #     credit_id: int
# #     id: str
# #     person_id: int
# #     character: Optional[str] = None
# #     role: str
