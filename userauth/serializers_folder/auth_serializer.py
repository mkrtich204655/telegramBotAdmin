from rest_framework import serializers


class AuthSerializerSendCode(serializers.Serializer):
    user_id = serializers.IntegerField(max_value=999999, min_value=100000, required=True, error_messages={
            'required': 'The user ID is required.',
            'invalid': 'The user ID must be a valid integer.',
            'min_value': 'The user ID must be at least 6 digits.',
            'max_value': 'The user ID cannot be more than 6 digits.',
        })


class AuthSerializerAuth(AuthSerializerSendCode):
    user_id = serializers.IntegerField(max_value=999999, min_value=100000, required=True, error_messages={
            'required': 'The user ID is required.',
            'invalid': 'The user ID must be a valid integer.',
            'min_value': 'The user ID must be at least 6 digits.',
            'max_value': 'The user ID cannot be more than 6 digits.',
        })
    OTP = serializers.IntegerField(write_only=True, max_value=999999, min_value=100000, required=True, error_messages={
            'required': 'The Password is wrong.',
            'invalid': 'The Password is wrong.',
            'min_value': 'The Password is wrong.',
            'max_value': 'The Password is wrong.',
        })

