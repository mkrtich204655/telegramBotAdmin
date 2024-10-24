from rest_framework import serializers


class RatingSerializer(serializers.Serializer):
    rating = serializers.IntegerField(error_messages={
            'invalid': 'The rating must be a valid integer.',
        })
    scumbags = serializers.IntegerField(error_messages={
            'invalid': 'The scumbags must be a valid integer.',
        })
    blocked_until = serializers.DateField(error_messages={
            'invalid': 'The blocked_until must be a valid date.',
        })

    def to_representation(self, instance):
        result = super(RatingSerializer, self).to_representation(instance)
        data = {
            'rating': result['rating'],
            'scumbags': result['scumbags'],
            'blocked_until': result['blocked_until'],
        }
        return data


