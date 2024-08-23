from django.contrib import admin

from rides.models import Ride

# Register your models here.


@admin.register(Ride)
class RideAdmin(admin.ModelAdmin):
    list_display = (
        'user_name', 'user_id', 'from_city', 'to_city', 'ride_date', 'ride_time', 'places', 'free_places',
        'price', 'car_mark', 'car_number', 'car_color')
    search_fields = ('user_name', 'from_city', 'to_city', 'car_number')
    list_filter = ('ride_date', 'ride_time', 'from_city', 'to_city')
    ordering = ('ride_date', 'ride_time')
