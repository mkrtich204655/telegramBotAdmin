from django.db.models import Q, Prefetch
from django.utils.timezone import now

from ride.models import Booking, Ride
from users.models import CustomUser


class UserService:

    def __init__(self):
        self.model = CustomUser.objects

    def get_user_with_relation(self, user_id):
        current_datetime = now()
        current_date = current_datetime.date()
        current_time = current_datetime.time()

        passenger_queryset = Booking.objects.filter(
            Q(ride__date=current_date, ride__time__gt=current_time, passenger_id=user_id) |
            Q(ride__date__gt=current_date, passenger_id=user_id)
        ).order_by('ride__date', 'ride__time')
        user_queryset = Ride.objects.filter(
            Q(date=current_date, time__gt=current_time, user_id=user_id) |
            Q(date__gt=current_date, user_id=user_id)
        ).order_by('date', 'time')

        return self.model.prefetch_related(
            'ratings',
            'history',
            Prefetch('passenger', queryset=passenger_queryset),
            Prefetch('user', queryset=user_queryset),
            'cars'
        ).filter(id=user_id).first()


    def get_user_by_TUID(self, id):
        return self.model.get(Q(tuid=id) | Q(id=id))

    def create_user_name_and_TUID(self, username, tuid, phone):
        return self.model.create(username=username, tuid=tuid, phone=phone)

    def update_username(self, username, tuid):
        return self.model.filter(tuid=tuid).update(username=username)

    def update_phone(self, phone, tuid):
        return self.model.filter(tuid=tuid).update(phone=phone)

    def get_user_by_uuid(self, tuid):
        return self.model.filter(uuid=tuid).first()