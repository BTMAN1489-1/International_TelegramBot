from aiogram import types, md
from utils.misc import MessageDeleter


@dp.message_handler(state="*", content_types=types.ContentTypes.NEW_CHAT_MEMBERS)
@MessageDeleter(60)
async def new_member_handler(message: types.Message):
    for member in message.new_chat_members:
        if not member.is_bot:
            return await message.answer(
                text=bot_data('dialogs')['welcome'].format(username=md.hbold(member.full_name),
                                                           chatname=md.hbold(message.chat.full_name)))
