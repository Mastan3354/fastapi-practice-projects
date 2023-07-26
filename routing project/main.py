from fastapi import FastAPI
from routers import test1, test2

app = FastAPI()


app.include_router(test1.router)
app.include_router(test2.router)