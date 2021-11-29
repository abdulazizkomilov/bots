import logging

from aiogram import Bot, Dispatcher, executor, types

from googletrans import Translator
translator = Translator()

API_TOKEN = '2113362402:AAHOISfKIJDQrnBleEGDXjA1SdbpNFy56f0'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):

    await message.reply("Salom!\nMen sizga tarjimonlik qilaman!\nMarxamat foydalaning.")

@dp.message_handler(commands=['help'])
async def send_helper(message: types.Message):

    await message.reply("Bu bot sizga tarjimonlik qiladi. Siz uz-en yoki en-uz da foydalanishingiz mumkin.")

@dp.message_handler()
async def tarjimon(message: types.Message):
    lang = translator.detect(message.text).lang
    dest = 'uz' if lang == 'en' else 'en'
    await message.reply(translator.translate(message.text, dest).text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)