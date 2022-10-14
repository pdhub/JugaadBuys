from typing import Optional

from fastapi import FastAPI, Request
import numpy as np
import pickle
popular_df = pickle.load(open('popular.pkl','rb'))
books = pickle.load(open('books.pkl','rb'))
pt = pickle.load(open('pt.pkl','rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl','rb'))
app = FastAPI()

@app.get('/')
def root():
    return 'ok'


@app.get('/item/{id}')
def read_item(id: int):
    return id


@app.get("/recommend/")
def recommend(bookName: Optional[str]=None):
    index = np.where(pt.index==bookName)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x:x[1],reverse=True)[1:6]
    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author']))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M']))
        data.append(item)
    return data