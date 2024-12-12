from rest_framework.viewsets import ViewSet
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from users.models import CustomUser
from users.serializers_folder.user_api_serializer import UserApiSerializer
from telegram_bot.encode import encrypt_json
from users.services.user_service import UserService


class UserView(ViewSet):
    @csrf_exempt
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.encrypt = encrypt_json
        self.userSerializer = UserApiSerializer
        self.service = UserService()

    def get_user_by_TUID(self, request):
        data = self.userSerializer(data=request.dec_body)

        if data.is_valid():
            validated_data = data.validated_data
            tuid = validated_data['tuid']
            username = validated_data['username']
            try:
                user = self.service.get_user_by_TUID(tuid)
            except CustomUser.DoesNotExist:
                user = self.service.create_user_name_and_TUID(username=username, tuid=tuid)
            except Exception as e:
                return JsonResponse(self.encrypt({'message': str(e)}), status=500)

            result = self.userSerializer(user).data
            return JsonResponse(self.encrypt(result), status=200)
        else:
            return JsonResponse(self.encrypt(data.errors), status=400)
