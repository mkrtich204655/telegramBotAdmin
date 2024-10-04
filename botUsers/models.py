from django.db import models


# Create your models here.

class BotUsers(models.Model):
    user_id = models.BigIntegerField()
    user_name = models.CharField(max_length=100, db_collation='utf8mb4_unicode_ci', null=True)
    bad_rating = models.IntegerField()
    blocked_until = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"ID: {self.user_id}"
