from rest_framework import serializers

from users.serializers_folder.history_serializer import HistorySerializer
from users.serializers_folder.rating_serializer import RatingSerializer


class UserSerializer(serializers.Serializer):
    rating = serializers.SerializerMethodField()
    history = serializers.SerializerMethodField()

    uuid = serializers.IntegerField(max_value=999999, min_value=100000, error_messages={
            'invalid': 'The uuid must be a valid integer.',
            'max_length': 'The uuid must be at least 6 digital long.',
        })
    tuid = serializers.IntegerField(error_messages={
        'invalid': 'The tuid must be a valid integer.',
    })
    username = serializers.CharField(max_length=50, error_messages={
        'invalid': 'The username must be a valid text.',
        'max_length': 'The username must be at least 50 characters long.',
    })
    phone = serializers.IntegerField(error_messages={
        'invalid': 'The phone must be a valid Integer.',
    })
    is_active = serializers.BooleanField(error_messages={
        'invalid': 'The is_active must be a valid boolean.',
    })

    def get_rating(self, obj):
        rating = obj.ratings.first()
        return RatingSerializer(rating).data if rating else {}

    def get_history(self, obj):
        history = obj.history.first()
        return HistorySerializer(history).data if history else {}
