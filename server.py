import requests
import codecs
from dataclasses import dataclass
from pydantic import BaseModel, Field
from fastapi import FastAPI, Request, logger
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from utils import assistant, salebot
from aiogram import Bot
from config import load_config

config = load_config("config/config.json", "config/texts.yml")
bot = Bot(token=config.tg_bot.token, parse_mode='HTML')

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


@app.post("/smarti/start", name="Wellcome")
async def user(request_: Request):
    data = await request_.json()
    client_id = data.get("user_id")
    message = Message(text=data.get("message"))
    api_key = data.get("api_key")
    print(await request_.body())
    mes = await salebot.sync_send_message(api_key=api_key, client_id=client_id, message=config.misc.messages.start)
    await assistant.request(message, client_id, start=True)


@app.post("/smarti")
async def user(request_: Request):
    print(await request_.body())
    data = await request_.json()
    client_id = data.get("user_id")
    telegram_id = data.get("telegram_id")
    message = Message(text=data.get("message"))
    print(message)
    if not message:
        return
    if message.text == "/start":
        await salebot.sync_send_message(api_key=api_key, client_id=client_id, message=config.misc.messages.start)
        await assistant.request(message, client_id, start=True)
        return
    api_key = data.get("api_key")
    mes = await bot.send_message(telegram_id, "Набираю сообщение...")

    response = await assistant.request(message, client_id, api_key=api_key)
    await bot.delete_message(mes.chat.id, mes.message_id)
    await salebot.sync_send_message(api_key=api_key, client_id=client_id, message=response)


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000, root_path="/api_v2")
