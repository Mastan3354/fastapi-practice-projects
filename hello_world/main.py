from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello_world():
    return {"message":"welcome to the world of python"}