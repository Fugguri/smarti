import os
from .GPTService import GPTService
from .AssistantService import AssistantService
from .GoogleService import GoogleService
from config import cfg
# gpt_service = GPTService(api_key=cfg.tg_bot.openai)
google = GoogleService()
try:
    assistant = AssistantService(api_key=cfg.tg_bot.openai)
except Exception as ex:
    print(ex)
