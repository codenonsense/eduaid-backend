from fastapi import FastAPI
from db import mongo_connect

# from routes.auth import auth_router
from routes.recommendations import recommendation_router
from routes.summaries import summaries_router
from routes.qna import qna_router
from routes.chat import chat_router

app = FastAPI()

# app.include_router(auth_router)
app.include_router(recommendation_router)
app.include_router(summaries_router)
app.include_router(qna_router)
app.include_router(chat_router)


@app.get("/")
def read_root():
    mongo_connect()
    return {"Hello": "World"}