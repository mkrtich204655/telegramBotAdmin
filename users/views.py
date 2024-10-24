import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from users.models import CustomUser, Rating, History
from users.serializers_folder.user_serializer import UserSerializer
from users.serializers_folder.user_api_serializer import UserApiSerializer

# Create your views here.

@csrf_exempt
def getUserByTUID(request):
    if request.method == 'POST':
        data = UserApiSerializer(data=json.loads(request.body))
        if data.is_valid():
            data = data.validated_data
            tuid = data['tuid']
            username = data['username']
            try:
                user = CustomUser.objects.get(tuid=tuid)
            except CustomUser.DoesNotExist:
                user = CustomUser.objects.create_user(username=username, tuid=tuid)
            except Exception as e:
                return JsonResponse(e.__context__, status=500)

            result = UserApiSerializer(user).data
            return JsonResponse(result, status=200)
        else:
            return JsonResponse(data=data.errors, status=400)


def getUserWithRelation(user_id):
    user = CustomUser.objects.prefetch_related('ratings', 'history').filter(id=user_id).first()
    return UserSerializer(user).data
