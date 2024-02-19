import requests
import codecs
from dataclasses import dataclass
from pydantic import BaseModel, Field
from fastapi import FastAPI, Request, logger
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from utils import assistant
app = FastAPI(
    title="Neur",
    summary="",
    version="0.1.1",
    description="some desc",
)


origins = [
    "http://localhost:3000",
    "http://localhost:8080",
    "http://localhost:8000",

]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Income_message(BaseModel):
    user_id: str
    message: str


@dataclass
class Message:
    id: int = None
    text: str = None


@app.get("/", name="Wellcome", tags=["Основное"], description="Тут будет описание методов?")
async def user():
    return {"message": "success"}


@app.post("/smarti/start", name="Wellcome", tags=["Основное"], description="Тут будет описание методов?")
async def user(request_: Request):
    print(await request_.body())
    data = await request_.json()
    user_id = data.get("user_id")
    message = Message(text=data.get("message"))
    api_key = data.get("api_key")
    response = await assistant.request(message, user_id, start=True)


@app.post("/smarti", name="Wellcome", tags=["Основное"], description="Тут будет описание методов?")
async def user(request_: Request):
    print(await request_.body())
    data = await request_.json()
    user_id = data.get("user_id")
    message = Message(text=data.get("message"))
    if not message:
        return
    api_key = data.get("api_key")
    print(data)
    # print(await request.json())
    response = await assistant.request(message, user_id)
    # return {"answer": response}
    params = {"message": response, "client_id": user_id}
    url = f'https://chatter.salebot.pro/api/{api_key}/message'
    req = requests.post(url, json=params)
    print(req)
if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000, root_path="/api_v2")
