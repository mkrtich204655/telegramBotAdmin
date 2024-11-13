import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.viewsets import ViewSet

from ride.serializers_folder.ride_serializer import RideSerializer
from users.serializers_folder.user_api_serializer import UserApiSerializer
from telegram_bot.decode import decrypt_json
from telegram_bot.encode import encrypt_json
from ride.services.ride_service import RideService
from users.services.user_service import UserService


class RideView(ViewSet):
    @csrf_exempt
    def __init__(self,  **kwargs):
        super().__init__(**kwargs)
        self.decrypt = decrypt_json
        self.encrypt = encrypt_json
        self.userSerializer = UserApiSerializer
        self.service = RideService()
        self.userService = UserService()

    def publish(self, request):
        decode_data = self.decrypt(json.loads(request.body))
        ride_serializer = RideSerializer(data=decode_data)

        if ride_serializer.is_valid():
            ride_data = ride_serializer.validated_data

            print(ride_data['user_id'])
            user = self.userService.get_user_by_TUID(ride_data['user_id'])
            if user is None:
                return JsonResponse(self.encrypt({'error': 'User not found'}), status=404)

            rides = self.service.check_ride_by_time(user.id, ride_data['date'], ride_data['time'])
            if rides is not None:
                print('bad ride checking')
                print(rides)
                return JsonResponse(self.encrypt(RideSerializer(rides).data), status=401)

            new_ride = self.service.create_ride(ride_data)
            print('good ride checking')
            return JsonResponse(self.encrypt(RideSerializer(new_ride).data), safe=False, status=201)
        else:
            print(ride_serializer.errors)
            return JsonResponse(self.encrypt(ride_serializer.errors), safe=False, status=400)

    def get_list(self, request):
        pass

    def show(self, request):
        pass

    def cancel(self, request):
        pass




