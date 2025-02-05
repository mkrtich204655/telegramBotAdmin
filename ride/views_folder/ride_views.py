from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.viewsets import ViewSet
from ride.serializers_folder.ride_serializer import RideSerializer, RideModelSerializer, RideDetailSerializer, RideDetailForPassengerSerializer
from users.serializers_folder.user_api_serializer import UserApiSerializer
from telegram_bot.encode import encrypt_json
from ride.services.ride_service import RideService
from users.services.user_service import UserService
from telegramBotAdmin.services import map_service


class RideView(ViewSet):
    @csrf_exempt
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.encrypt = encrypt_json
        self.userSerializer = UserApiSerializer
        self.service = RideService()
        self.userService = UserService()
        self.modelSerializer = RideModelSerializer()

    def publish(self, request):
        ride_serializer = RideSerializer(data=request.dec_body)

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

            new_ride = self.service.create_ride(self.modelSerializer.to_dict(ride_data))
            print('good ride checking')
            return JsonResponse(self.encrypt(RideSerializer(new_ride).data), safe=False, status=201)
        else:
            print(ride_serializer.errors)
            return JsonResponse(self.encrypt(ride_serializer.errors), safe=False, status=400)

    def get_list(self, request):
        ride_list_serializer = RideSerializer(data=request.dec_body)
        if ride_list_serializer.is_valid():
            ride_data = ride_list_serializer.validated_data

            print(ride_data['user_id'])
            user = self.userService.get_user_by_TUID(ride_data['user_id'])
            if user is None:
                return JsonResponse(self.encrypt({'error': 'User not found'}), status=404)
            ride_data['user_id'] = user.id
            rides_list = self.service.get_all_rides(ride_data)
            # if ride_data['action'] == 'passenger':
            return JsonResponse(self.encrypt(RideDetailForPassengerSerializer(rides_list, many=True).data), safe=False, status=200)
            # else: 
            #     return JsonResponse(self.encrypt(RideDetailForPassengerSerializer(rides_list, many=True).data), safe=False, status=200)
        else:
            print(ride_list_serializer.errors)
            return JsonResponse(self.encrypt(ride_list_serializer.errors), safe=False, status=400)

    def show(self, request):
        ride_list_serializer = RideSerializer(data=request.dec_body)
        if ride_list_serializer.is_valid():
            ride_data = ride_list_serializer.validated_data

            ride = self.service.get_ride_by_id(ride_data)
            if ride_data['action'] == 'passenger':
                return JsonResponse(self.encrypt(RideDetailForPassengerSerializer(ride).data), safe=False, status=200)
            else:
                return JsonResponse(self.encrypt(RideDetailSerializer(ride).data), safe=False, status=200)
        else:
            print(ride_list_serializer.errors)
            return JsonResponse(self.encrypt(ride_list_serializer.errors), safe=False, status=400)

    def cancel(self, request):
        ride_serializer = RideSerializer(data=request.dec_body)
        if ride_serializer.is_valid():
            ride_data = ride_serializer.validated_data
            self.service.cancel_ride_by_id(ride_data['id'])
            return JsonResponse(self.encrypt({"status": True, "text": "ride was cancelled"}), safe=False, status=200)
        else:
            return JsonResponse(self.encrypt({"status": False, "text": "something went wrong"}), safe=False, status=500)
