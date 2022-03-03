import logging
from aiogram import Bot, Dispatcher, executor, types

from oxfordLookup import getDefinitions
from googletrans import Translator
translator = Translator()

API_TOKEN = '5173514989:AAHw_d9Q3iHm0ct6u5g3sR_KpVCUH50udsk'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("""Salom!
    
Men Oxford Dictionary Bot_man! 
So`z yuboring va so`zning ma`lolarini ko`rsataman.

Misol uchun: apple
 👇 👇 👇
Word: Apple
Definitions:

👉 the round fruit of a tree of the rose family, which typically has thin green or red skin and crisp flesh.

👉 the tree bearing apples, with hard pale timber that is used in carpentry and to smoke food.

Yoki istalgan gapni tarjima qilib beraman!""")


@dp.message_handler()
async def tarjimon(message: types.Message):
    print(message)
    lang = translator.detect(message.text).lang
    if len(message.text.split()) > 2:
        dest = 'uz' if lang == 'en' else 'en'
        await message.reply(translator.translate(message.text, dest).text)
    else:
        if lang=='en':
            word_id = message.text
        else:
            word_id = translator.translate(message.text, dest='en').text

        lookup = getDefinitions(word_id)
        if lookup:
            await message.reply(f"Word: {word_id} \nDefinitions:\n{lookup['definitions']}")
            if lookup.get('audio'):
                await message.reply_voice(lookup['audio'])
        else:
            await message.reply("Bunday so'z topilmadi")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)