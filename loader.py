def get_dispatcher():
    from aiogram import Bot, Dispatcher, types
    from data import BotAppData
    from aiogram.contrib.fsm_storage.memory import MemoryStorage
    return Dispatcher(bot=Bot(BotAppData.API_TOKEN, parse_mode=types.ParseMode.HTML), storage=MemoryStorage())
