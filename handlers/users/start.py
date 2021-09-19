from aiogram import types, md
from aiogram.utils import emoji
from aiogram.dispatcher.filters import CommandStart, ChatTypeFilter


@dp.message_handler(ChatTypeFilter(chat_type=types.ChatType.PRIVATE), CommandStart(), state="*")
async def bot_start(message: types.Message, *args, **kwargs):
    await message.answer(emoji.emojize(
        _(bot_data('dialogs')['start_text']).format(username=md.hbold(message.from_user.full_name))))
