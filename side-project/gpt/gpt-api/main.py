from fastapi import FastAPI
from open_ai.routes import chat_router

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI"}


# Chatgpt API Endpoint
app.include_router(chat_router, prefix="/chat",  tags=['chats'])



