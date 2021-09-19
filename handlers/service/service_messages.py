from aiogram.types import ContentType, Message
from utils.misc import MessageDeleter


@dp.message_handler(
    content_types=(ContentType.DELETE_CHAT_PHOTO, ContentType.NEW_CHAT_PHOTO, ContentType.NEW_CHAT_TITLE,
                   ContentType.LEFT_CHAT_MEMBER))
@MessageDeleter(60)
async def bot_start(message: Message):
    pass
