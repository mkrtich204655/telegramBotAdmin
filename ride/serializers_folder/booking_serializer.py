from rest_framework import serializers
from ride.serializers_folder.ride_serializer import RideSerializer


class BookingSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False, allow_null=True, error_messages={
        'invalid': 'The ID must be a valid integer.'
    })
    places = serializers.IntegerField(required=False, allow_null=True, error_messages={
        'invalid': 'The Places must be a valid integer.'
    })
    total_price = serializers.IntegerField(required=False, allow_null=True, error_messages={
        'invalid': 'The Price must be a valid integer.'
    })
    passenger_id = serializers.IntegerField(required=False, allow_null=True, error_messages={
        'invalid': 'The Passenger ID must be a valid integer.'
    })
    ride_id = serializers.IntegerField(required=False, allow_null=True, error_messages={
        'invalid': 'The Ride ID must be a valid integer.'
    })


class BookingDetailSerializer(BookingSerializer):
    ride = serializers.SerializerMethodField()

    def get_ride(self, obj):
        ride = obj.ride
        print(ride.__dict__, 'from serializer booking', 'ride')
        return RideSerializer(ride).data if ride else {}


class BookingModelSerializer:
    def to_dict(self, obj):
        return {
            "passenger_id": obj['passenger_id'],
            "ride_id": obj['ride_id'],
            "places": obj['places'],
            "total_price": 0,
        }
