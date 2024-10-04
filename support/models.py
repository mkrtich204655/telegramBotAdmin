from django.db import models


class Support(models.Model):
    user_id = models.BigIntegerField()
    user_name = models.CharField(max_length=100, db_collation='utf8mb4_unicode_ci')
    user_message = models.TextField(max_length=1000, db_collation='utf8mb4_unicode_ci')
    support_message = models.TextField(max_length=1000, db_collation='utf8mb4_unicode_ci', null=True)
    date = models.DateField()
    status = models.IntegerField()

    def __str__(self):
        return self.user_name
