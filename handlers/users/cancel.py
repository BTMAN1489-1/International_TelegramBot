from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram import types


@dp.message_handler(commands='cancel', state='*')
@dp.message_handler(Text(equals='cancel', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext, *args, **kwargs):
    """
    Allow user to cancel any action
    """
    current_state = await state.get_state()
    print(current_state)
    if current_state is None:
        return
    # Cancel state and inform user about it
    await message.reply('Cancelled.')
    await state.finish()

