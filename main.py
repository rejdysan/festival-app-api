from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Festival(BaseModel):
    title: str
    description: str
    includes_food: bool = True
    rating: Optional[int] = None

@app.get("/hello")
def root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    return {"data": "Posts"}

@app.post("/create")
def create(festival: Festival):
    return festival