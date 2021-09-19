from typing import Union

from .config import BotAppData, I18NData


def get_bot_data():
    import ujson
    from collections import namedtuple

    with open('data/bot_dialogs.json', 'r') as data:
        bot_dialogs = ujson.load(data)
    with open('data/bot_commands.json', 'r') as data:
        bot_commands = ujson.load(data)

    def wrapped(data_name: str, settings: str = None) -> Union[list, dict]:
        """Returning bot data

        The data_name argument takes str, for example: "commands" or "dialogs".
        The settings argument takes str, for example: "commands" or "dialogs".
        The function that returns a dict of the bot`s data.
        If data_name not in ("commands", "dialogs"), raise ValueError.

        :param settings: Optional[str]
        :param data_name: str
        :return: Union[list, dict]
        """
        if data_name == 'commands':
            Command = namedtuple("Command", ["name", "description"])
            if settings == "default":
                return [Command(name, description) for name, description in bot_commands["default_commands"].items()]
            elif settings == "only_admin":
                return [Command(name, description) for name, description in bot_commands["admin_commands"].items()]
            raise ValueError('Invalid parameter settings')
        elif data_name == 'dialogs':
            return bot_dialogs
        raise ValueError('Invalid parameter data_name')

    return wrapped
