from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData


class WelcomeStateInlineKeyboard:
    age_callback = CallbackData('age', 'sign_num')
    success_callback = CallbackData('success', 'value')

    @classmethod
    def create_age_keyboard(cls):
        return InlineKeyboardMarkup(inline_keyboard=
                                    [[InlineKeyboardButton(text='-5',
                                                           callback_data=cls.age_callback.new(sign_num=-5)),
                                      InlineKeyboardButton(text='-1',
                                                           callback_data=cls.age_callback.new(sign_num=-1)),
                                      InlineKeyboardButton(text='+1',
                                                           callback_data=cls.age_callback.new(sign_num=1)),
                                      InlineKeyboardButton(text='+5',
                                                           callback_data=cls.age_callback.new(sign_num=5))],
                                     [InlineKeyboardButton(text=_('Confirm'),
                                                           callback_data='success')]], row_width=4)
