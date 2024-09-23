# Generated migration file for Ride, Book, and Cities models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ride_id', models.IntegerField()),
                ('booked_places', models.IntegerField()),
                ('passenger_name', models.CharField(max_length=100, db_collation='utf8mb4_unicode_ci')),
                ('passenger_id', models.BigIntegerField()),
            ],
        ),
    ]
