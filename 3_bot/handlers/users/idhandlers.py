from aiogram import types
from aiogram.dispatcher import filters

from loader import dp

SUPERUSERS = [2000000, 3000000, 874354497]
BLACKLIST = [4000000, 5000000]

@dp.message_handler(chat_id=SUPERUSERS, text='secret')
async def id_filter_example(msg: types.Message):
    await msg.answer("Xush kelibsiz!")