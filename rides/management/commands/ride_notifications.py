import asyncio
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from asgiref.sync import sync_to_async

from books.models import Book
from telegram_bot.main import send_message
from rides.models import Ride


class Command(BaseCommand):
    help = 'Task that runs every hour'

    def handle(self, *args, **kwargs):
        asyncio.run(self.run())

    async def run(self):
        rides = await sync_to_async(self.get_rides)()
        if not rides:
            return False
        for ride in rides:
            bookings = await sync_to_async(self.get_bookings)(ride.id)
            bookings_list = await sync_to_async(list)(bookings)

            if bookings_list:
                text_for_driver = (f"❗️❗️ ՀԻՇԵՑՈՒՄ ❗️❗\n\n"
                                   f"Ողջույն սիրելի @{ride.user_name},️\n"
                                   f"Դուք ունեք հրապարակված ուղևորություն ժամը {ride.ride_time}\n"
                                   f"Ուղղությունը {ride.from_city}ից {ride.to_city}\n\n"
                                   f"Ձեր ուղևորների ցուցակը\n"
                                   f"____________________\n")

                for booking in bookings_list:
                    text_for_passengers = (f"❗️❗️ ՀԻՇԵՑՈՒՄ ❗️❗️\n\n"
                                           f"Ողջույն սիրելի @{booking.passenger_name}\n"
                                           f"Դուք ունեք ամրագրված ուղևորություն ժամը {ride.ride_time} \n "
                                           f"Տեղերի քանակը {booking.booked_places}. գումարի չափ {ride.price * booking.booked_places} դրամ \n"
                                           f"Ուղղությունը {ride.from_city}ից {ride.to_city}\n"
                                           f"{ride.car_color} {ride.car_mark} {ride.car_number}\n"
                                           f"Վարորդ @{ride.user_name}: վճարման տեսակը` կանխիկ")
                    text_for_driver += (f"@{booking.passenger_name}. {booking.booked_places} Տեղ. {ride.price * booking.booked_places} դրամ\n"
                                        f"____________________\n")

                    await send_message(booking.passenger_id, text_for_passengers)
                await send_message(ride.user_id, text_for_driver)
            else:
                text_for_driver = (f"❗️❗️ ՀԻՇԵՑՈՒՄ ❗️❗\n\n"
                                   f"Ողջույն սիրելի @{ride.user_name},️\n"
                                   f"Դուք ունեք հրապարակված ուղևորություն ժամը {ride.ride_time}\n"
                                   f"Ուղղությունը {ride.from_city}ից {ride.to_city}\n\n"
                                   f"Ցավոք, մինչ այս պահը դեռ ոչ ոք տեղեր չի ամրագրել։\n\n"
                                   f"❗️ ԿԱՐԵՎՈՐ Է ❗️\n"
                                   f"Այս հիշեցումից հետո տեղեր ամրագրելիս բոտն այլևս չի հիշեցնի ձեզ,"
                                   f" բայց դուք կստանաք ծանուցում ստանդարտ ամրագրելիս")
                await send_message(ride.user_id, text_for_driver)

    @staticmethod
    def get_rides():
        today = datetime.now().date()
        current_time = datetime.now()

        one_hour_later = current_time + timedelta(hours=1)

        rides = list(Ride.objects.filter(
            ride_date=today,
            ride_time=one_hour_later.strftime("%H") + ":00",
        ))
        return rides or None

    @staticmethod
    def get_bookings(ride_id):
        return Book.objects.filter(ride_id=ride_id)


if __name__ == "__main__":
    Command().handle()
