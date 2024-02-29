import os
# from .GPTService import GPTService
from .AssistantServiceds import AssistantService
from .GoogleService import GoogleService
from config import cfg
from .SaleBotService import SalebotService
# gpt_service = GPTService(api_key=cfg.tg_bot.openai)
salebot = SalebotService()
google = GoogleService()
try:
    assistant = AssistantServiceds(api_key=cfg.tg_bot.openai)
except Exception as ex:
    print(ex)
