from django.db import models


# Create your models here.

class Book(models.Model):
    ride_id = models.IntegerField()
    booked_places = models.IntegerField()
    passenger_name = models.CharField(max_length=100)
    passenger_id = models.IntegerField()
