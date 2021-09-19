import asyncio
import logging
from contextlib import suppress
from functools import wraps

from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.utils.exceptions import MessageCantBeDeleted, MessageToDeleteNotFound


class MessageDeleter:
    def __init__(self, sleep_time: int, incoming: bool = True, outgoing: bool = False):
        self.sleep_time = sleep_time
        self.incoming = incoming
        self.outgoing = outgoing

    def __call__(self, callback):
        @wraps(callback)
        async def wrapped(in_message, *args, **kwargs):
            out_message = await callback(in_message, *args, **kwargs)
            try:
                if self.incoming:
                    if not isinstance(in_message, types.Message):
                        raise CancelHandler('Invalid type received. Make sure the Update is of type Message')
                    else:
                        asyncio.create_task(self._delete_message(in_message, self.sleep_time))
                if self.outgoing:
                    if not isinstance(out_message, types.Message):
                        raise CancelHandler('Invalid type received. Make sure the Update is of type Message')
                    else:
                        asyncio.create_task(self._delete_message(out_message, self.sleep_time))
            except CancelHandler:
                logging.exception('Invalid type received')

        return wrapped

    @classmethod
    async def _delete_message(cls, message: types.Message, sleep_time: int):
        await asyncio.sleep(sleep_time)
        with suppress(MessageCantBeDeleted, MessageToDeleteNotFound):
            await message.delete()
