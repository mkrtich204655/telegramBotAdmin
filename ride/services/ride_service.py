from datetime import timedelta, datetime, date

from asgiref.sync import async_to_sync
from django.db.models import Q, F
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram_bot.main import send_message
from ride.models import Ride


class RideService:
    def __init__(self):
        self.model = Ride.objects

    def create_ride(self, data):
        return self.model.create(**data)

    def check_ride_by_time(self, user_id, rdate, time):
        time_plus_one_hour = (datetime.combine(datetime.today(), time) + timedelta(hours=1)).time()
        time_minus_one_hour = (datetime.combine(datetime.today(), time) - timedelta(hours=1)).time()
        return self.model.filter(
            Q(user_id=user_id) &
            Q(date=rdate) &
            Q(time__gte=time_minus_one_hour) &
            Q(time__lte=time_plus_one_hour)
        ).first()

    def get_all_rides(self, data: dict):
        query = ''
        print(data)
        related = ['from_city', 'to_city', 'car']
        if data['action'] == 'driver':
            query = Q(user_id=data['user_id']) & Q(date__gte=date.today())
        elif data['action'] == 'passenger':
            related.append('user')
            query = Q(date=data['date']) & Q(from_city=data['from_city_id']) & Q(to_city=data['to_city_id']) & Q(
                free_places__gte=data['free_places']) & ~Q(user_id=data['user_id'])

        return self.model.prefetch_related(*related).filter(query)

    def get_ride_by_id(self, data: dict):
        related = ['from_city', 'to_city', 'car']
        if data['action'] == 'passenger':
            related.append('user')

        return self.model.prefetch_related(*related).filter(id=data['id']).first()

    def cancel_ride_by_id(self, ride_id):
        ride = self.model.filter(id=ride_id).first()
        passengers = ride.rider.all()
        if passengers:
            for passenger in passengers:
                ride_text = "cancelled text"
                markup = InlineKeyboardMarkup([
                    [InlineKeyboardButton('YES', callback_data=f"suggestRide_{str(ride.from_city_id)}"
                                                               f"_{str(ride.to_city_id)}_{str(ride.date)}"
                                                               f"_{str(passenger.places)}")]
                ])

                print(passenger, passenger.passenger, passenger.passenger.tuid)
                async_to_sync(send_message)(passenger.passenger.tuid, ride_text, markup)
                passenger.delete()

            history = ride.user.history.first()
            history.rides = F('rides') - 1
            history.cancelled = F('cancelled') + 1
            history.save()
            rating = ride.user.ratings.first()
            if rating.rating > 0:
                rating.rating = F('rating') - 1
                rating.save()

        return ride.delete()
