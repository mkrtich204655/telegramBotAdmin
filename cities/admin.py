from django.contrib import admin

from cities.models import Cities

# Register your models here.


@admin.register(Cities)
class CitiesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)