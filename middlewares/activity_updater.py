# from database.Database import update_user_status

# from aiogram import types
# from aiogram.dispatcher import FSMContext, middlewares


# class ActivityUpdaterMiddleware(middlewares.BaseMiddleware):
#     def __init__(self):
#         super().__init__()

#     async def on_process_message(self, message: types.Message, data: dict):
#         try:
#             telegram_id=message.from_user.id
#             update_user_status(telegram_id)
#         except:
#             pass
