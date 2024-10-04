from django.db import models

class Ride(models.Model):
    objects = None
    user_name = models.CharField(max_length=50)
    user_id = models.IntegerField()
    from_city = models.CharField(max_length=50)
    to_city = models.CharField(max_length=50)
    ride_date = models.DateField()
    ride_time = models.CharField(max_length=10)
    places = models.IntegerField()
    free_places = models.IntegerField()
    price = models.IntegerField()
    car_number = models.CharField(max_length=10)
    car_mark = models.CharField(max_length=50)
    car_color = models.CharField(max_length=50)

    def __str__(self):
        return f"ID:{self.id} - UID: {self.user_id} - FC: {self.from_city} - TC: {self.to_city}"
