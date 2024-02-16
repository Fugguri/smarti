from aiogram import types
from aiogram import Dispatcher
from aiogram.dispatcher.handler import ctx_data
from aiogram.dispatcher import FSMContext

# from utils import gpt_service
from utils import assistant
from config.config import Config
from keyboards.keyboards import Keyboards
from .admin import admin


async def start(message: types.Message, state: FSMContext):
    cfg: Config = ctx_data.get()['config']
    kb: Keyboards = ctx_data.get()['keyboards']
    await message.answer(cfg.misc.messages.start)
    response = await assistant.request(message, message.from_user.id, start=True)


async def receive_message(message: types.Message, state: FSMContext):
    print(message)
    cfg: Config = ctx_data.get()['config']
    kb: Keyboards = ctx_data.get()['keyboards']
    # response = gpt_service.query_index(message.text, message.from_user.id)
    # print(gpt_service.dialog_summary())
    wait_message = await message.answer("Набираю сообщение...")
    response = await assistant.request(message, message.from_user.id)
    await wait_message.delete()
    await message.reply(response)


def register_user_handlers(dp: Dispatcher, kb: Keyboards):
    dp.register_message_handler(start, commands=["start"], state="*")
    dp.register_message_handler(receive_message,  state="*")
