from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()

class Festival(BaseModel):
    title: str
    description: str
    includes_food: bool = True
    rating: Optional[int] = None

my_festivals = []

@app.get("/festivals")
def get_festivals():
    return {"data": my_festivals}

@app.post("/festivals")
def create_festival(festival: Festival):
    festival_dict = festival.dict()
    festival_dict['id'] = randrange(0, 1000000)
    my_festivals.append(festival_dict)
    return festival