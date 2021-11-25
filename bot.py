import logging
import wikipedia

from aiogram import Bot, Dispatcher, executor, types
wikipedia.set_lang('uz')

API_TOKEN = '2114389627:AAEUU1eDbrsMg96Ga1CbrTY5ujImCGBdu-w'
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
    await message.reply("Hi!\nWelcome to wikibot!")
    await message.reply("Bu bot siz kiritgan so'zga doir malumotlarni wikipediadan topib beradi.")


@dp.message_handler()
async def sendwiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Bu mavzuga doir maqola topilmadi")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)