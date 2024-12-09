from django.db.models import F
from django.db.models.signals import post_save, pre_delete, pre_save
from django.dispatch import receiver

from users.models import CustomUser
from .models import Ride, Booking
from cities.models import Cities


@receiver(pre_save, sender=Booking)
def call(sender, instance, **kwargs):
    ride = instance.ride
    ride.free_places = F('free_places') - instance.places
    ride.save()
    ride.refresh_from_db()
    if instance.id:
        instance.total_price = F('total_price') + (ride.price * instance.places)
        instance.places = F('places') + instance.places
    else:
        instance.total_price = ride.price * instance.places
    increment_passenger_activity(instance.passenger)


@receiver(pre_delete, sender=Booking)
def call(sender, instance, **kwargs):
   pass


@receiver(post_save, sender=Ride)
def call(sender, instance, **kwargs):
    if not instance.id:
        increment_driver_activity(instance)
    increment_cities_usage(instance)


def increment_ride_places(instance, **kwargs):
    pass


def decrement_ride_places(instance, **kwargs):
    pass


def increment_cities_usage(ride):
    Cities.objects.filter(id__in=[ride.from_city.id, ride.to_city.id]).update(usage=F('usage') + 1)


def increment_driver_activity(ride):
    history = ride.user.history.first()
    if history:
        history.activity = F('activity') + 1
        history.rides = F('rides') + 1
        history.save()


def increment_passenger_activity(passenger):
    history = passenger.history.first()
    if history:
        history.activity = F('activity') + 1
        history.bookings = F('bookings') + 1
        history.save()


