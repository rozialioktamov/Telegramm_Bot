import logging

from aiogram import Bot, Dispatcher, executor, types

import wikipedia

wikipedia.set_lang('UZ')
API_TOKEN = '5503629274:AAGj1UEKAE_Uezw6Q9IVSLnTrY6kSWCYwyY'

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
    await message.reply("Assalomu alaykum!\nWikipedia botiga xush kelibsiz!\nBot @developer2006 tomonidan\n yaratilgan.")

@dp.message_handler()
async def echo(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("bu mavzuga oid\n maqola yo'q")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)