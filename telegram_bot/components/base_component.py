from asgiref.sync import async_to_sync
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram_bot.main import send_message


class BaseComponent:

    def __init__(self):
        self.async_call = async_to_sync
        self.markup = InlineKeyboardMarkup
        self.button = InlineKeyboardButton
        self.send = send_message
