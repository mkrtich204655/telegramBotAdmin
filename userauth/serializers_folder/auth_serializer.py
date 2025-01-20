from rest_framework import serializers


class AuthSerializerSendCode(serializers.Serializer):
    uuid = serializers.IntegerField(max_value=999999, min_value=100000, required=True, error_messages={
            'required': 'The user UUID is required.',
            'invalid': 'The user UUID must be a valid integer.',
            'min_value': 'The user UUID must be at least 6 digits.',
            'max_value': 'The user UUID cannot be more than 6 digits.',
        })


class AuthSerializerAuth(AuthSerializerSendCode):
    password = serializers.IntegerField(write_only=True, max_value=999999, min_value=100000, required=True, error_messages={
            'required': 'The Password is wrong.',
            'invalid': 'The Password is wrong.',
            'min_value': 'The Password is wrong.',
            'max_value': 'The Password is wrong.',
        })

