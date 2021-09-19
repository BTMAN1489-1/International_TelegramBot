import logging
from aiogram import Dispatcher
from data import BotAppData


async def on_startup_notify(dp: Dispatcher):
    for admin in BotAppData.ADMINS:
        try:
            await dp.bot.send_message(admin, "Бот Запущен")

        except Exception as err:
            logging.exception(err)
