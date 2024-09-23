from django.contrib import admin

from support.models import Support

# Register your models here.


@admin.register(Support)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'user_name', 'support_message', 'date', 'status')
    search_fields = ('user_id', 'user_name', 'date', 'status')
    list_filter = ('date', 'status', 'user_id')