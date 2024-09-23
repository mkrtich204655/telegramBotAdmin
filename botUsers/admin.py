from django.contrib import admin

from botUsers.models import BotUsers

# Register your models here.


@admin.register(BotUsers)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'user_name', 'bad_rating', 'blocked_until')
    search_fields = ('user_id', 'user_name', 'bad_rating', 'blocked_until')
    list_filter = ('bad_rating', 'blocked_until')