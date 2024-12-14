from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.viewsets import ViewSet
from ride.serializers_folder.booking_serializer import BookingSerializer, BookingModelSerializer, \
    BookingDetailSerializer
from telegram_bot.encode import encrypt_json
from ride.services.booking_service import BookingService
from users.services.user_service import UserService


class BookingView(ViewSet):
    @csrf_exempt
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.encrypt = encrypt_json
        self.service = BookingService()
        self.userService = UserService()
        self.bookingModelSerializer = BookingModelSerializer()

    def booking(self, request):
        booking_serializer = BookingSerializer(data=request.dec_body)

        if booking_serializer.is_valid():
            booking_data = booking_serializer.validated_data

            print(booking_data['passenger_id'])
            user = self.userService.get_user_by_TUID(booking_data['passenger_id'])
            if user is None:
                return JsonResponse(self.encrypt({'error': 'User not found'}), status=404)
            booking_data['passenger_id'] = user.id
            new_booking = self.service.update_or_create_booking(self.bookingModelSerializer.to_dict(booking_data))
            print(new_booking)
            return JsonResponse(self.encrypt(BookingDetailSerializer(new_booking).data), safe=False, status=201)
        else:
            print(booking_serializer.errors)
            return JsonResponse(self.encrypt(booking_serializer.errors), safe=False, status=400)

    def get_list(self, request):
        booking_serializer = BookingSerializer(data=request.dec_body)

        if booking_serializer.is_valid():
            booking_data = booking_serializer.validated_data

            user = self.userService.get_user_by_TUID(booking_data['passenger_id'])
            if user is None:
                return JsonResponse(self.encrypt({'error': 'User not found'}), status=404)
            booking_data['passenger_id'] = user.id
            booking_list = self.service.get_list(booking_data['passenger_id'])
            return JsonResponse(self.encrypt(BookingDetailSerializer(booking_list, many=True).data), safe=False,
                                status=201)
        else:
            print(booking_serializer.errors)
            return JsonResponse(self.encrypt(booking_serializer.errors), safe=False, status=400)

    def show(self, request):
        booking_serializer = BookingSerializer(data=request.dec_body)

        if booking_serializer.is_valid():
            booking_data = booking_serializer.validated_data

            user = self.userService.get_user_by_TUID(booking_data['passenger_id'])
            if user is None:
                return JsonResponse(self.encrypt({'error': 'User not found'}), status=404)

            booking_data['passenger_id'] = user.id
            booking_data = self.service.get_one(booking_data)
            return JsonResponse(self.encrypt(BookingDetailSerializer(booking_data).data), safe=False,
                                status=201)
        else:
            print(booking_serializer.errors)
            return JsonResponse(self.encrypt(booking_serializer.errors), safe=False, status=400)

    def cancel(self, request):
        booking_serializer = BookingSerializer(data=request.dec_body)

        if booking_serializer.is_valid():
            booking_data = booking_serializer.validated_data

            self.service.cancel(booking_data['id'])
            return JsonResponse(self.encrypt({"message": 'success'}), safe=False,
                                status=201)
        else:
            print(booking_serializer.errors)
            return JsonResponse(self.encrypt(booking_serializer.errors), safe=False, status=400)
