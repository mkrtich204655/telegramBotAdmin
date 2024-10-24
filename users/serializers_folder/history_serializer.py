from rest_framework import serializers


class HistorySerializer(serializers.Serializer):
    rides = serializers.IntegerField(error_messages={
        'invalid': 'The rides must be a valid integer.',
    })
    bookings = serializers.IntegerField(error_messages={
            'invalid': 'The bookings must be a valid integer.',
        })
    activity = serializers.IntegerField(error_messages={
            'invalid': 'The activity must be a valid integer.',
        })
    saved = serializers.IntegerField(error_messages={
            'invalid': 'The saved must be a valid integer.',
        })
    spend = serializers.IntegerField(error_messages={
            'invalid': 'The spend must be a valid integer.',
        })
    cancelled = serializers.IntegerField(error_messages={
            'invalid': 'The cancelled must be a valid integer.',
        })

    def to_representation(self, instance):
        result = super(HistorySerializer, self).to_representation(instance)
        data = {
            'rides': result['rides'],
            'bookings': result['bookings'],
            'activity': result['activity'],
            'saved': result['saved'],
            'spend': result['spend'],
            'cancelled': result['cancelled'],
        }
        return data
