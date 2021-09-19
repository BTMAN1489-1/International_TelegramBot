from aiogram import types, md
from aiogram.dispatcher.filters.builtin import CommandHelp
from aiogram.utils import emoji


@dp.message_handler(CommandHelp(), state="*")
async def bot_help(message: types.Message, *args, **kwargs):
    reply = await message.reply(
        emoji.emojize(_(bot_data('dialogs')['help_text']).format(
            botname=md.hbold((await message.bot.me).full_name))))
