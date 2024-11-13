from rest_framework import serializers
from ride.models import Booking


class BookingSerializer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(
        queryset=Booking.objects.all(),
        error_messages={
            'does_not_exist': 'The booking ID does not exist.',
            'incorrect_type': 'The booking ID must be a valid integer.'
        }
    )

    def to_representation(self, instance):
        result = super(BookingSerializer, self).to_representation(instance)
        data = {
            'model': result['model'],
            'color': result['color'],
            'number': result['number'],
        }
        return data

