from fastapi import FastAPI, Depends
import models
from sqlalchemy.orm import Session
from database import Base, engine
import schemas
from helper_functions import get_db,http_exception,successful_response


app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/")
def read_all(db: Session = Depends(get_db)):
    try:
        return db.query(models.Movies).all()
    except Exception as e:
        return {"status":500,"message":str(e)}


@app.get("/{movie_id}")
def read_all(movie_id: int, db: Session = Depends(get_db)):
    try:
        movie_data=db.query(models.Movies).filter(models.Movies.id==movie_id).first()
        if movie_data is not None:
            return movie_data
        return http_exception()
    except Exception as e:
        return {"status":500,"message":str(e)}


@app.post("/")
def create_movie(movie: schemas.Movie, db: Session = Depends(get_db)):
    try:
        movie_model = models.Movies()
        movie_model.name=movie.name
        movie_model.actor=movie.actor
        db.add(movie_model)
        db.commit()
        return successful_response(201)
    except Exception as e:
        return {"status":500,"message":str(e)}


@app.put("/{movie_id}")
def update_movie(movie_id: int, movie: schemas.Movie, db: Session = Depends(get_db)):
    try:
        movie_model = db.query(models.Movies).filter(models.Movies.id == movie_id).first()
        if movie_model is None:
            return http_exception()
        movie_model.name=movie.name
        movie_model.actor = movie.actor
        db.add(movie_model)
        db.commit()
        return successful_response(200)
    except Exception as e:
        return {"status":500,"message":str(e)}


@app.delete("/{movie_id}")
def delete_movie(movie_id: int, db: Session = Depends(get_db)):
    try:
        movie_model = db.query(models.Movies).filter(models.Movies.id == movie_id).first()
        if movie_model is None:
            return http_exception()
        db.query(models.Movies).filter(models.Movies.id == movie_id).delete()
        db.commit()
        return successful_response(200)
    except Exception as e:
        return {"status":500,"message":str(e)}

    
