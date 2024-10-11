import os
from telegram import Bot
from telegram.request import HTTPXRequest

request = HTTPXRequest(pool_timeout=5)
bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
bot = Bot(token=bot_token,  request=request)


async def send_message(chat_id, text, markup=None):
    await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup)
