from aiogram import types
from utils.misc import MessageDeleter


@dp.message_handler(state=None)
@MessageDeleter(10, outgoing=True)
async def bot_echo_all(message: types.Message, *args, **kwargs):
    return await message.answer(message.text)
