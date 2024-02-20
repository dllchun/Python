from fastapi import APIRouter, Depends, Request
from open_ai.service import OpenAIClient
from dotenv import dotenv_values
from open_ai.model import Prompt

config = dotenv_values(".env")
chat_router = APIRouter()


@chat_router.get("/", description="Send a new chat request to gpt")
async def chat(prompt: Prompt):
    client = OpenAIClient(openai_api_key=config["openai-key"])
    try:
        if prompt.text:
            response = client.chat_completion(prompt)
            return {"response": response}
    except Exception as e:
        print(e)

