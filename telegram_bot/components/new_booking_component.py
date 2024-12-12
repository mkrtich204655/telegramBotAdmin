from telegram_bot.components.base_component import BaseComponent


class NewBooking(BaseComponent):

    def __init__(self):
        super().__init__()

    def call(self, chat_id, passenger):
        ride_text = f"new booking text @{passenger.username}"
        self.async_call(self.send)(chat_id, ride_text)
