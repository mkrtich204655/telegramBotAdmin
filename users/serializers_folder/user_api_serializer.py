from rest_framework import serializers


class UserApiSerializer(serializers.Serializer):
    tuid = serializers.IntegerField(required=True, write_only=True, error_messages={
            'invalid': 'The tuid must be a valid integer.',
            'required': 'The tuid field is required.',
        })
    uuid = serializers.IntegerField(required=False, error_messages={
            'invalid': 'The uuid must be a valid integer.',
        })
    is_active = serializers.BooleanField(required=False, error_messages={
            'invalid': 'The uuid must be a valid integer.',
            'max_length': 'The uuid must be at least 6 digital long.',
        })
    username = serializers.CharField(max_length=50, required=False, error_messages={
            'invalid': 'The username must be a valid text.',
            'max_length': 'The username must be at least 50 characters long.',
        })

    def to_representation(self, instance):
        result = super(UserApiSerializer, self).to_representation(instance)
        return {
            "uuid": result["uuid"],
            "is_active": result["is_active"],
        }
