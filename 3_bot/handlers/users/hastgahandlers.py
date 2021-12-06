from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from loader import dp

@dp.message_handler(hashtags='money')
@dp.message_handler(cashtags=['eur', 'usd'])
async def hashtag_example(msg: types.Message):
    await msg.reply('Yee akang kuchaydi.')