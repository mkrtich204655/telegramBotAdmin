from django.http import JsonResponse
from rest_framework.viewsets import ViewSet
from django.views.decorators.csrf import csrf_exempt
from cities.models import Cities
from telegram_bot.encode import encrypt_json
from cities.cities_serializer import CitiesSerializer


class CitiesView(ViewSet):
    @csrf_exempt
    def __init__(self):
        super().__init__()
        pass

    def index(self, request):
        try:
            serializer = CitiesSerializer(Cities.objects.all(), many=True).data
            return JsonResponse(encrypt_json({'cities': serializer}), status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
