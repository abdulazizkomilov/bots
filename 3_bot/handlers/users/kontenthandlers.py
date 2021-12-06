from aiogram import types
from aiogram.dispatcher import filters

from loader import dp

# @dp.message_handler(content_types=types.ContentTypes.PHOTO)


@dp.message_handler(content_types='photo')
async def photo_handler(msg: types.Message):
    await msg.answer('Nima rasm bu?')

@dp.message_handler(content_types='sticker')
async def photo_handler(msg: types.Message):
    await msg.answer('==')

@dp.message_handler(content_types='voice')
async def photo_handler(msg: types.Message):
    await msg.answer('Tushunmadim?')

@dp.message_handler(content_types=types.ContentTypes.LOCATION)
async def photo_handler(msg: types.Message):
    await msg.answer('Nimaning locationni?')