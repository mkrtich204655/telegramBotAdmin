from django.db import models


# Create your models here.

class Support(models.Model):
    user_id = models.BigIntegerField()
    user_name = models.CharField(max_length=100, db_collation='utf8mb4_unicode_ci')
    support_message = models.TextField(max_length=1000, db_collation='utf8mb4_unicode_ci')
    date = models.DateField()
    status = models.IntegerField()
