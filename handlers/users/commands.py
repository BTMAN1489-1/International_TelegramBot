from aiogram import types, md
from aiogram.dispatcher.filters import Command, AdminFilter


@dp.message_handler(AdminFilter(), Command("commands"), state="*")
async def send_commands(message: types.Message, *args, **kwargs):
    bot = message.bot
    commands = await bot.get_my_commands(scope=types.BotCommandScopeAllChatAdministrators())

    await bot.send_message(chat_id=message.from_user.id, text="".join((_(bot_data('dialogs')['commands_text']), '\n'.join(
        map(lambda command: f"<b>/{md.quote_html(command.command)}</b>: <b>{_(command.description)}</b>", commands)))),
                           reply_to_message_id=message.message_id, allow_sending_without_reply=True)


@dp.message_handler(Command("commands"), state="*")
async def send_commands(message: types.Message, *args, **kwargs):
    bot = message.bot
    commands = await bot.get_my_commands(scope=types.BotCommandScopeDefault())
    await bot.send_message(chat_id=message.from_user.id, text="".join((_(bot_data('dialogs')['commands_text']), '\n'.join(
        map(lambda command: f"<b>/{md.quote_html(command.command)}</b>: <b>{_(command.description)}</b>", commands)))),
                           reply_to_message_id=message.message_id, allow_sending_without_reply=True)

