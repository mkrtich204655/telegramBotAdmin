from telegram_bot.components.base_component import BaseComponent


class BookingCancel(BaseComponent):

    def __init__(self):
        super().__init__()

    def call(self, chat_id):
        ride_text = "cancelled booking text"

        self.async_call(self.send)(chat_id, ride_text)
