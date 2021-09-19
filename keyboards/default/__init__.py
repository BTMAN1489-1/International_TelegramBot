from aiogram.types.reply_keyboard import ReplyKeyboardMarkup, KeyboardButton


class WelcomeStateKeyboard:
    @classmethod
    def create_gender_keyboard(cls):
        return ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Male'), KeyboardButton(text='Female')]],
                                   resize_keyboard=True, input_field_placeholder=_('What\'s your gender?'))
