from datetime import timedelta, datetime, date

from django.db.models import Q
from telegram_bot.components.ride_cancel_component import RideCancel
from ride.models import Ride


class RideService:
    def __init__(self):
        self.model = Ride.objects
        self.telebot_cancel_call = RideCancel()

    def create_ride(self, data):
        return self.model.create(**data)

    def check_ride_by_time(self, user_id, ride_date, time):
        time_plus_one_hour = (datetime.combine(datetime.today(), time) + timedelta(hours=1)).time()
        time_minus_one_hour = (datetime.combine(datetime.today(), time) - timedelta(hours=1)).time()
        return self.model.filter(
            Q(user_id=user_id) &
            Q(date=ride_date) &
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
                self.telebot_cancel_call.call(passenger, ride)
                passenger.delete()

        return ride.delete()
