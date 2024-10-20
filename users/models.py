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

    def generate_uuid(self):
        while True:
            random_number = str(random.randint(100000, 999999))

            if not CustomUser.objects.filter(uuid=random_number).exists():
                return random_number
