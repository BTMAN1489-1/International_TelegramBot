import asyncio
from aiogram.utils.executor import start_polling
import logging
from loader import get_dispatcher
import middlewares
import filters
import handlers
from data import get_bot_data
from utils.misc import bot_logging, setup_builtins
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


def load_dependencies(dispatcher):
    bot_logging.setup_loggers()
    middlewares.setup_middleware(dispatcher)
    filters.setup_filters(dispatcher)
    setup_builtins.set_scope((('bot_data', get_bot_data()), ("dp", dispatcher)))
    handlers.setup_handlers()


async def on_startup(dispatcher):
    logging.warning('Run setup bot dependencies')
    await asyncio.to_thread(load_dependencies, dispatcher)
    await asyncio.gather(set_default_commands(dispatcher),
                         on_startup_notify(dispatcher))
    logging.warning('Finish setup bot dependencies')


async def on_shutdown(dispatcher):
    logging.warning('Shutting down bot dependencies')
    await asyncio.gather(dispatcher.bot.delete_webhook(),
                         dispatcher.storage.close(),
                         dispatcher.storage.wait_closed())
    logging.warning('All bot dependencies are closed')


if __name__ == '__main__':
    try:
        start_polling(get_dispatcher(), on_startup=on_startup, on_shutdown=on_shutdown)
    except Exception as ex:
        logging.exception('FatalBotError: %s' % ex)
    else:
        logging.warning('Bot closed successfully')
