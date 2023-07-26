from database import SessionLocal
from fastapi import HTTPException


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

def http_exception():
    return HTTPException(status_code=404,detail="Movie not found")

def successful_response(status_code: int):
    return {
        "status":status_code,
        "transaction": "successful"
    }