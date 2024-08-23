from django.contrib import admin

from books.models import Book

# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'ride_id', 'passenger_name', 'passenger_id', 'booked_places')
    search_fields = ('passenger_name',)
    list_filter = ('ride_id',)