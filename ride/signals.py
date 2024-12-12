from django.db.models import F
from django.db.models.signals import post_save, pre_delete, pre_save
from django.dispatch import receiver
from .models import Ride, Booking
from cities.models import Cities


@receiver(pre_save, sender=Booking)
def call(sender, instance, **kwargs):
    ride = instance.ride
    decrement_ride_places(instance, ride)
    increment_passenger_activity(instance, instance.passenger, ride)
    if instance.id:
        booking = Booking.objects.filter(id=instance.id).first()
        instance.total_price = booking.total_price + (ride.price * instance.places)
        instance.places = booking.places + instance.places
    else:
        instance.total_price = (ride.price * instance.places)
    increment_cities_usage(ride)


@receiver(pre_delete, sender=Booking)
def call(sender, instance, **kwargs):
    increment_ride_places(instance, instance.ride)
    decrement_passenger_activity(instance, instance.passenger)


@receiver(pre_save, sender=Ride)
def call(sender, instance, **kwargs):
    if not instance.id:
        increment_driver_activity(instance)
        increment_cities_usage(instance)


@receiver(pre_delete, sender=Ride)
def call(sender, instance, **kwargs):
    print(instance, "ride instance pre_delete")
    passengers = Booking.objects.filter(ride_id=instance.id).first()
    if passengers:
        decrement_driver_activity(instance)
        decrement_driver_rating(instance)


def decrement_driver_rating(instance):
    rating = instance.user.ratings.first()
    if rating.rating > 0:
        rating.rating -= 1
        rating.save()


def decrement_driver_activity(instance):
    history = instance.user.history.first()
    history.cancelled += 1
    history.save()


def increment_ride_places(instance, ride):
    ride.free_places += instance.places
    ride.save()
    driver_history = ride.user.history.first()
    new_spend = (ride.price * instance.places)
    if driver_history.saved >= new_spend:
        driver_history.saved -= new_spend
    driver_history.save()


def decrement_ride_places(instance, ride):
    if ride.free_places >= instance.places:
        ride.free_places -= instance.places
    driver_history = ride.user.history.first()
    driver_history.saved += (ride.price * instance.places)
    driver_history.save()
    ride.save()


def increment_cities_usage(ride):
    Cities.objects.filter(id__in=[ride.from_city.id, ride.to_city.id]).update(usage=F('usage') + 1)


def increment_driver_activity(ride):
    history = ride.user.history.first()
    if history:
        history.activity += 1
        history.rides += 1
        history.save()


def increment_passenger_activity(instance, passenger, ride):
    history = passenger.history.first()
    if history:
        history.activity += 1
        history.bookings += instance.places
        history.spend += instance.places * ride.price
        history.save()


def decrement_passenger_activity(instance, passenger):
    history = passenger.history.first()
    if history.activity > 0:
        history.activity -= 1
    if history.spend >= instance.total_price:
        history.spend -= instance.total_price
    if history.bookings >= instance.places:
        history.bookings -= instance.places
    history.save()


