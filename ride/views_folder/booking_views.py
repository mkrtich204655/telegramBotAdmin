from django.views.decorators.csrf import csrf_exempt
from rest_framework.viewsets import ViewSet

from users.serializers_folder.user_api_serializer import UserApiSerializer
from telegram_bot.decode import decrypt_json
from telegram_bot.encode import encrypt_json
from ride.services.booking_service import BookingService


class BookingView(ViewSet):
    @csrf_exempt
    def __init__(self,  **kwargs):
        super().__init__(**kwargs)
        self.decrypt = decrypt_json
        self.encrypt = encrypt_json
        self.userSerializer = UserApiSerializer
        self.service = BookingService()

    def booking(self, request):
        pass

    def get_list(self, request):
        pass

    def show(self, request):
        pass

    def cancel(self, request):
        pass




