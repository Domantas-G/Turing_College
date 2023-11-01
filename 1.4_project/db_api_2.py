from fastapi import FastAPI, HTTPException, Depends
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()


@app.get("/")
def read_something():
    return {"msg": "something"}
