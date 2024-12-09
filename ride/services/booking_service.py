from django.db.models import F, Q

from ride.models import Booking


class BookingService:
    def __init__(self):
        self.model = Booking.objects

    def update_or_create_booking(self, data):
        booking = self.model.filter(Q(ride_id=data['ride_id']) & Q(passenger_id=data['passenger_id'])).first()
        if booking:
            booking.places = data['places']
            booking.save()
        else:
            booking = self.model.create(**data)
        booking.refresh_from_db()
        return booking


