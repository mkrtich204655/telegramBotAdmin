from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import Ride, Booking


@receiver(post_save, sender=Booking)
def call(sender, instance, **kwargs):
    increment_city_usage(instance, **kwargs)
    increment_user_activity(instance, **kwargs)
    increment_ride_places(instance, **kwargs)


@receiver(pre_delete, sender=Booking)
def decrement_ride_places(sender, instance, **kwargs):
   pass


@receiver(post_save, sender=Ride)
def call(sender, instance, **kwargs):
    increment_city_usage(instance, **kwargs)
    increment_user_activity(instance, **kwargs)


@receiver(pre_delete, sender=Ride)
def call(sender, instance, **kwargs):
    decrement_user_rating(instance, **kwargs)
    suggest_rides(instance, **kwargs)


def increment_city_usage(instance, **kwargs):
    pass


def increment_user_activity(instance, **kwargs):
    pass


def increment_ride_places(instance, **kwargs):
    pass


def suggest_rides(instance, **kwargs):
    pass


def decrement_user_rating(instance, **kwargs):
    pass
