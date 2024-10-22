import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from users.models import CustomUser


# Create your views here.

def getUserById(uuid):
    user = CustomUser.objects.filter(uuid=uuid).first() or None
    return user


@csrf_exempt
def getUserByTUID(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        tuid = data['tuid']
        username = data['username']
        user = CustomUser.objects.filter(tuid=tuid).values('uuid', 'is_active').first()
        if user is None:
            new_user = CustomUser.objects.create_user(username=username, tuid=tuid)
            data = {
                "uuid": new_user.uuid,
                "is_active": new_user.is_active,
            }
        else:
            data = {
                "uuid": user['uuid'],
                "is_active": user['is_active'],
            }

        return JsonResponse(data, status=200)
