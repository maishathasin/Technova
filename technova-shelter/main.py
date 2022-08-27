from typing import Union

from fastapi import FastAPI
from model import model

app = FastAPI()


@app.get("/")
def read_stock(q: Union[str, None] = None): #optional parameter for now
    return model('pictures/banana and apple2.jpeg')


#hardcoded picture path, 