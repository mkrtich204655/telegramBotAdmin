from datetime import timedelta, datetime

from django.db.models import Q

from ride.models import Ride



class RideService:
    def __init__(self):
        self.model = Ride

    def create_ride(self, data):
        return self.model.objects.create(**data)

    def check_ride_by_time(self, user_id, date, time):
        time_plus_one_hour = (datetime.combine(datetime.today(), time) + timedelta(hours=1)).time()
        time_minus_one_hour = (datetime.combine(datetime.today(), time) - timedelta(hours=1)).time()
        return self.model.objects.filter(
            Q(user_id=user_id) &
            Q(date=date) &
            Q(time__gte=time_minus_one_hour) &
            Q(time__lte=time_plus_one_hour)
        ).first()

