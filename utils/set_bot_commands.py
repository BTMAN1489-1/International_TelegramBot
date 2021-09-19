async def set_default_commands(dp):
    from aiogram import types
    await dp.bot.set_my_commands(
        commands=[types.BotCommand(command.name, command.description) for command in bot_data("commands", "default")],
        scope=types.BotCommandScopeDefault())
    # await dp.bot.set_my_commands(commands=bot_commands.admin_command, scope=types.BotCommandScopeAllChatAdministrators())
