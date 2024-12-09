from django.db import models
from cities.models import Cities
from users.models import CustomUser, Cars


class Ride(models.Model):
    from_city = models.ForeignKey(Cities, on_delete=models.DO_NOTHING, related_name='from_city')
    to_city = models.ForeignKey(Cities, on_delete=models.DO_NOTHING, related_name='to_city')
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, related_name='user')
    car = models.ForeignKey(Cars, on_delete=models.DO_NOTHING, related_name='car')
    places = models.IntegerField(default=0)
    free_places = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    baggage = models.BooleanField(default=False)
    date = models.DateField()
    time = models.TimeField()


class Booking(models.Model):
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE, related_name='rider')
    places = models.IntegerField(default=1)
    passenger = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='passenger')
    total_price = models.IntegerField(default=0)






