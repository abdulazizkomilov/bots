from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp



@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer(f"Echo bot. "
                         f"Sizning xabar:\n"
                         f"{message.text}")