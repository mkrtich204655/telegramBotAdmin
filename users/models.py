import random

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    uuid = models.IntegerField(unique=True, editable=False)
    tuid = models.BigIntegerField(unique=True, default=None, null=True)
    phone = models.BigIntegerField(unique=True, default=None, null=True)
    username = models.CharField(max_length=150, unique=True, null=True)
    first_name = models.CharField(max_length=150, null=True)
    last_name = models.CharField(max_length=150, null=True)
    email = models.CharField(max_length=150, null=True)
    password = models.CharField(max_length=128, null=True, verbose_name='password')

    def generate_uuid(self):
        while True:
            random_number = str(random.randint(100000, 999999))

            if not CustomUser.objects.filter(uuid=random_number).exists():
                return random_number


class Rating(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='ratings')
    rating = models.IntegerField(default=0)
    scumbags = models.IntegerField(default=0)
    blocked_until = models.DateTimeField(null=True)


class History(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='history')
    rides = models.IntegerField(default=0)
    bookings = models.IntegerField(default=0)
    activity = models.IntegerField(default=0)
    saved = models.IntegerField(default=0)
    spend = models.IntegerField(default=0)
    cancelled = models.IntegerField(default=0)


class Cars(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='cars')
    model = models.CharField(max_length=150)
    number = models.CharField(max_length=10, unique=True)
    color = models.CharField(max_length=50)
