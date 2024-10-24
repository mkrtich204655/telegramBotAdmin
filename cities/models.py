from django.db import models


# Create your models here.

class Cities(models.Model):
    name = models.CharField(max_length=100)
    usage = models.IntegerField(default=0, null=True)
