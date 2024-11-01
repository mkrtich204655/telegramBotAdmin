import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from users.models import CustomUser
from users.serializers_folder.user_serializer import UserSerializer
from users.serializers_folder.user_api_serializer import UserApiSerializer
from telegram_bot.decode import decrypt_json
from telegram_bot.encoding import encrypt_json

# Create your views here.

@csrf_exempt
def getUserByTUID(request):
    if request.method == 'POST':
        decode_data = decrypt_json(json.loads(request.body))
        data = UserApiSerializer(data=decode_data)
        if data.is_valid():
            data = data.validated_data
            tuid = data['tuid']
            username = data['username']
            try:
                user = CustomUser.objects.get(tuid=tuid)
            except CustomUser.DoesNotExist:
                user = CustomUser.objects.create_user(username=username, tuid=tuid)
            except Exception as e:
                return JsonResponse(encrypt_json({'message': e.__context__}), status=500)

            result = UserApiSerializer(user).data
            return JsonResponse(encrypt_json(result), status=200)
        else:
            return JsonResponse(encrypt_json(data.errors), status=400)


def getUserWithRelation(user_id):
    user = CustomUser.objects.prefetch_related('ratings', 'history').filter(id=user_id).first()
    return UserSerializer(user).data
