from typing import Optional

from fastapi import FastAPI, Request

app = FastAPI()

@app.get('/')
def root():
    return 'ok'


@app.get('/item/{id}')
def read_item(id: int):
    return id


@app.get("/recommend/")
def recommend(bookName: Optional[str]=None):
    return bookName;
