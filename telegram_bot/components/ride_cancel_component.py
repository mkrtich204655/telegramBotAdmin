from telegram_bot.components.base_component import BaseComponent


class RideCancel(BaseComponent):

    def __init__(self):
        super().__init__()

    def call(self, passenger, ride):
        ride_text = "cancelled ride text"
        markup = self.markup([
            [self.button('YES', callback_data=f"suggestRide_{str(ride.from_city_id)}"
                                              f"_{str(ride.to_city_id)}_{str(ride.date)}"
                                              f"_{str(passenger.places)}")]
        ])

        self.async_call(self.send)(passenger.passenger.tuid, ride_text, markup)
