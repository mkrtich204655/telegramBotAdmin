# Generated migration file for Ride, Book, and Cities models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('user_id', models.IntegerField()),
                ('from_city', models.CharField(max_length=50)),
                ('to_city', models.CharField(max_length=50)),
                ('ride_date', models.DateField()),
                ('ride_time', models.CharField(max_length=10)),
                ('places', models.IntegerField()),
                ('free_places', models.IntegerField()),
                ('price', models.IntegerField()),
                ('car_number', models.CharField(max_length=10)),
                ('car_mark', models.CharField(max_length=50)),
                ('car_color', models.CharField(max_length=50)),
            ],
        ),
    ]
