from aiogram.dispatcher import FSMContext
from aiogram.types.reply_keyboard import ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text
from FSM import WelcomeState
from aiogram import types, md
from keyboards.default import WelcomeStateKeyboard
from keyboards.inline import WelcomeStateInlineKeyboard
import re


@dp.message_handler(commands=['welcome'], state=None)
async def welcome_start(message: types.Message, *args, **kwargs):
    await message.reply(_("Hi, What is your name?"))
    await WelcomeState.name.set()


@dp.message_handler(lambda message: message.text.isalnum(), state=WelcomeState.name)
async def welcome_name(message: types.Message, state: FSMContext, *args, **kwargs):
    async with state.proxy() as data:
        data['name'] = message.text
        data['age'] = 0
    await message.reply(_("Are you 0 years old?"), reply_markup=WelcomeStateInlineKeyboard.create_age_keyboard())
    await WelcomeState.next()


@dp.callback_query_handler(Text(contains='age'), state=WelcomeState.age)
async def welcome_age(call: types.CallbackQuery, state: FSMContext, *args, **kwargs):
    keyboard = WelcomeStateInlineKeyboard.create_age_keyboard()
    async with state.proxy() as data:
        age = data["age"]
        num = int(call.data.split(":")[-1])
        if age + num >= 0:
            data["age"] = age + num
            await call.message.edit_text(_('Are you {age} years old?').format(age=data["age"]), reply_markup=keyboard)
    await call.answer()


@dp.callback_query_handler(Text(contains='success'), state=WelcomeState.age)
async def welcome_age_success(call: types.CallbackQuery, state: FSMContext, *args, **kwargs):
    async with state.proxy() as data:
        await call.message.edit_text(_('I see you are {age} years old').format(age=data["age"]))
        await WelcomeState.next()
        await call.message.reply(_("What's your gender?"), reply_markup=WelcomeStateKeyboard.create_gender_keyboard())


@dp.message_handler(regexp=re.compile('male|female', re.IGNORECASE), state=WelcomeState.gender)
async def welcome_gen(message: types.Message, state: FSMContext, *args, **kwargs):
    async with state.proxy() as data:
        data['gender'] = message.text
        await message.answer(
            _('Your name: {name}. Your age: {age} years. Your gender: {gender}').format(
                name=md.hbold(data["name"].capitalize()), age=md.quote_html(data["age"]),
                gender=md.quote_html(data["gender"].capitalize())), reply_markup=ReplyKeyboardRemove())
    await state.finish()
