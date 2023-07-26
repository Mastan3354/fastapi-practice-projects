from fastapi import FastAPI
from pydantic import BaseModel
import json


app = FastAPI()

movies={
    1:{"name":"dhmaka","actor":"ravi teja"},
    2:{"name":"god father","actor":"chiranjeevi"},
    3:{"name":"rama rao","actor":"ravi teja"},
    4:{"name":"rrr","actor":"junior ntr"},
    5:{"name":"sarkaru vari pata","actor":"mahesh"},
    6:{"name":"radhe shyam","actor":"prabhas"}
}

def get_movie(id):
    try:
        movie=movies[id]
        return True
    except:
        return False
        

@app.get("/movies")
def get_all_movies():
    return movies


@app.get("/movies/{id}")
def get_all_movies(id: int):
    if get_movie(id):
        return movies.get(id)
    return {"response":f"movie with id {id} not exists"}


class Movie(BaseModel):
    name: str
    actor: str

@app.post("/movies/create")
def create_movie(data: Movie):
    try:
        movie_data={}
        item_id=0
        for item in data:
            movie_data[item[0]]=item[1]
        for movie in movies:
            if movie>item_id:
                item_id=movie
        movies[item_id+1]=movie_data
        return {"response":movies[item_id+1]}
    except Exception as e:
        return {"response":str(e)}


@app.put("/movies/update/{id}")
def update_movie(id: int, data: Movie):
    try:
        if get_movie(id):
            movie_data={}
            for item in data:
                movie_data[item[0]]=item[1]
            movies[id]=movie_data
            return {"response":movies[id]}
        return {"response":f"movie with id {id} not exists"}
    except Exception as e:
        return {"response":str(e)}


@app.delete("/movies/delete/{id}")
def update_movie(id: int):
    try:
        if get_movie(id):
            del movies[id]
            return {"response":f"deleted movie {id}"}
        return {"response":f"movie with id {id} not exists"}
    except Exception as e:
        return {"response":str(e)}


    