from django.http import JsonResponse
from rest_framework.viewsets import ViewSet
from users.serializers_folder.car_serializer import CarSerializer, CarCreateSerializer
from django.views.decorators.csrf import csrf_exempt
from users.services.cars_service import CarsService
from users.services.user_service import UserService
from telegram_bot.decode import decrypt_json
from telegram_bot.encode import encrypt_json
import json


class CarView(ViewSet):
    @csrf_exempt
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = CarsService()
        self.userService = UserService()
        self.decrypt = decrypt_json
        self.encrypt = encrypt_json

    def create_car(self, request):
        decode_data = self.decrypt(json.loads(request.body))
        car_serializer = CarCreateSerializer(data=decode_data)

        if car_serializer.is_valid():
            car_data = car_serializer.validated_data

            user = self.userService.get_user_by_TUID(car_data['tuid'])
            if user is None:
                return JsonResponse(self.encrypt({'error': 'User not found'}), status=404)

            car = self.service.check_car_by_user_id_and_number(user.id, car_data['number'])
            if car is not None:
                return JsonResponse(self.encrypt(CarSerializer(car).data), status=200)

            car_data.pop('tuid', None)
            car_data['user_id'] = user.id

            car = self.service.create_car(car_data)
            return JsonResponse(self.encrypt(CarSerializer(car).data), safe=False, status=201)
        else:
            return JsonResponse(self.encrypt(car_serializer.errors), safe=False, status=400)
