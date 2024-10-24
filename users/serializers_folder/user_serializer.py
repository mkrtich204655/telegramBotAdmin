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
    is_active = serializers.BooleanField(error_messages={
        'invalid': 'The is_active must be a valid boolean.',
    })

    def get_rating(self, obj):
        latest_rating = obj.ratings.first()
        return RatingSerializer(latest_rating).data if latest_rating else {}

    def get_history(self, obj):
        latest_history = obj.history.first()
        return HistorySerializer(latest_history).data if latest_history else {}
