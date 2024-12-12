from rest_framework import serializers

from cities.cities_serializer import CitySerializer
from users.serializers_folder.car_serializer import CarSerializer
from users.serializers_folder.user_serializer import UserSerializer


class RideModelSerializer:

    def to_dict(self, obj):
        return {
            "from_city_id": obj['from_city_id'],
            "to_city_id": obj['to_city_id'],
            "user_id": obj['user_id'],
            "car_id": obj['car_id'],
            "price": obj['price'],
            "places": obj['places'],
            "free_places": obj['free_places'],
            "date": obj['date'],
            "time": obj['time'],
            "baggage": obj['baggage'],
        }


class RideSerializer(serializers.Serializer):
    from_city = serializers.SerializerMethodField()
    to_city = serializers.SerializerMethodField()
    car = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    id = serializers.IntegerField(required=False, allow_null=True, error_messages={
        'invalid': 'The ID must be a valid integer.'
    })
    from_city_id = serializers.IntegerField(required=False, allow_null=True, error_messages={
        'invalid': 'The City ID must be a valid integer.'
    })
    to_city_id = serializers.IntegerField(required=False, allow_null=True, error_messages={
        'invalid': 'The City ID must be a valid integer.'
    })
    user_id = serializers.IntegerField(required=False, allow_null=True, error_messages={
        'invalid': 'The User ID must be a valid integer.'
    })
    car_id = serializers.IntegerField(required=False, allow_null=True, error_messages={
        'invalid': 'The Car ID must be a valid integer.'
    })
    price = serializers.IntegerField(allow_null=True, error_messages={
        'invalid': 'The Price must be a valid integer.'
    })
    places = serializers.IntegerField(allow_null=True, error_messages={
        'invalid': 'The Places must be a valid integer.'
    })
    free_places = serializers.IntegerField(allow_null=True, error_messages={
        'invalid': 'The Free Places must be a valid integer.'
    })
    date = serializers.DateField(allow_null=True, error_messages={
        'invalid': 'The Date must be a valid date.'
    })
    time = serializers.TimeField(allow_null=True, error_messages={
        'invalid': 'The Time must be a valid time.'
    })
    baggage = serializers.BooleanField(allow_null=True, error_messages={
        'invalid': 'The Baggage must be a valid boolean.'
    })
    action = serializers.CharField(required=False, allow_null=True, error_messages={
        'required': 'The action field is required.',
        'invalid': 'The action must be a valid text.'
    })

    def get_from_city(self, obj):
        city = obj.from_city
        return CitySerializer(city).data if city else {}

    def get_to_city(self, obj):
        city = obj.to_city
        return CitySerializer(city).data if city else {}

    def get_car(self, obj):
        car = obj.car
        return CarSerializer(car).data if car else {}

    def get_user(self, obj):
        user = obj.user
        return UserSerializer(user).data if user else {}


class RideDetailSerializer(RideSerializer):
    bookings = serializers.SerializerMethodField()

    def get_bookings(self, obj):
        bookings = obj.rider.all()
        return [{'places': booking.places, 'total_price': booking.total_price, 'passenger_id': booking.passenger.uuid,
                 'passenger_username': booking.passenger.username} for booking in bookings]
