from asgiref.sync import async_to_sync
from django.contrib import admin
from django.urls import path
from django.shortcuts import render, redirect
from django.utils.html import format_html
from support.models import Support
from support.forms import SendMessageForm
from telegram_bot.main import send_message

@admin.register(Support)
class SupportAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'user_name', 'user_message', 'support_message', 'date', 'status', 'send_message_link')
    search_fields = ('user_id', 'user_name', 'date', 'status')
    list_filter = ('date', 'status', 'user_id')
    ordering = ('date',)

    def send_message_link(self, obj):
        if obj.status == 0:
            return format_html(
                '<a class="button" href="{}">Answer</a>',
                f"/admin/support/support/{obj.id}/send_message/"
            )
        else:
            return format_html('<p> answered </p>')

    send_message_link.short_description = 'Send Message'
    send_message_link.allow_tags = True

    def send_message_view(self, request, object_id):
        support = self.get_object(request, object_id)

        if request.method == "POST":
            form = SendMessageForm(request.POST)
            if form.is_valid():
                message_text = form.cleaned_data['message_text']

                support.status = 1
                support.support_message = message_text
                support.save()
                chat_id = support.user_id
                async_to_sync(send_message)(chat_id, message_text, None)
                self.message_user(request, "Message sent successfully!")
                return redirect(f'/admin/support/support/')
        else:
            form = SendMessageForm()

        return render(request, 'admin/send_message.html', {'form': form, 'support': support})

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('<int:object_id>/send_message/', self.admin_site.admin_view(self.send_message_view), name='support-send-message'),
        ]
        return custom_urls + urls
