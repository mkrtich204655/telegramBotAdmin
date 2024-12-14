import os
import logging
from telegram import Bot
# from telegram.request import HTTPXRequest

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# request = HTTPXRequest(pool_timeout=500)
bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
bot = Bot(token=bot_token)


async def send_message(chat_id, text, markup=None):
    try:
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup)
    except Exception as e:
        logger.error(f"Failed to send message to {chat_id}: {e}")
