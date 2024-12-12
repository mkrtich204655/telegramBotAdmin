from django.db.models import Q
from django.utils.timezone import now
from datetime import timedelta
from telegram_bot.components.cancel_booking_component import BookingCancel
from telegram_bot.components.new_booking_component import NewBooking

from ride.models import Booking


class BookingService:
    def __init__(self):
        self.model = Booking.objects
        self.telebot_booking_cancel_call = BookingCancel()
        self.telebot_new_booking_call = NewBooking()

    def update_or_create_booking(self, data):
        booking = self.model.filter(Q(ride_id=data['ride_id']) & Q(passenger_id=data['passenger_id'])).first()
        if booking:
            booking.places = data['places']
            booking.save()
        else:
            booking = self.model.create(**data)
        booking.refresh_from_db()
        self.telebot_new_booking_call.call(booking.ride.user.tuid, booking.passenger)
        return booking

    def get_list(self, passenger_id):
        current_datetime = now()

        current_date = current_datetime.date()
        current_time_minus_one_hour = (current_datetime - timedelta(hours=1)).time()

        bookings = self.model.filter(
            Q(ride__date=current_date, ride__time__gt=current_time_minus_one_hour, passenger_id=passenger_id) |
            Q(ride__date__gt=current_date, passenger_id=passenger_id)
        ).order_by('ride__date', 'ride__time')
        return bookings

    def get_one(self, data):
        booking = self.model.filter(
            Q(id=data['id'], passenger_id=data['passenger_id'])
        ).first()
        return booking

    def cancel(self, booking_id):
        booking = self.model.filter(id=booking_id).first()
        self.telebot_booking_cancel_call.call(booking.ride.user.tuid)
        return booking.delete()
