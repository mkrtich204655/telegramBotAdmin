from django.db import models
from rides.models import Ride


# Create your models here.

class Book(models.Model):
    objects = None
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE, related_name='bookings')
    booked_places = models.IntegerField()
    passenger_name = models.CharField(max_length=100)
    passenger_id = models.IntegerField()
