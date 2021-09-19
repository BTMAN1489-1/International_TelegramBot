from aiogram.dispatcher.filters.state import State, StatesGroup


class WelcomeState(StatesGroup):
    name = State()  # Will be represented in storage as 'Form:name'
    age = State()  # Will be represented in storage as 'Form:age'
    gender = State()


