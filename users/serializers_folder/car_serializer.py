from rest_framework import serializers


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False, error_messages={
        'invalid': 'The id must be a valid integer.',
    })
    user_id = serializers.IntegerField(required=False, error_messages={
        'invalid': 'The user id must be a valid integer.',
    })
    model = serializers.CharField(max_length=50, required=True, error_messages={
        'required': 'The model is required.',
        'invalid': 'The model must be a valid text.',
        'max_length': 'The model must be at least 50 characters long.',
    })
    color = serializers.CharField(max_length=50, required=True, error_messages={
        'required': 'The color is required.',
        'invalid': 'The color must be a valid text.',
        'max_length': 'The color must be at least 50 characters long.',
    })
    number = serializers.CharField(max_length=7, required=True, error_messages={
        'required': 'The number is required.',
        'invalid': 'The number must be a valid text.',
        'max_length': 'The number must be at least 7 characters long.',
    })

    def to_representation(self, instance):
        result = super(CarSerializer, self).to_representation(instance)
        data = {
            'id': instance.id,
            'model': result['model'],
            'color': result['color'],
            'number': result['number'],
            'user_id': result['user_id'],
        }
        return data


class CarCreateSerializer(serializers.Serializer):
    tuid = serializers.IntegerField(required=True, error_messages={
        'required': 'The tuid is required.',
        'invalid': 'The tuid must be a valid integer.',
    })
    model = serializers.CharField(max_length=50, required=True, error_messages={
        'required': 'The model is required.',
        'invalid': 'The model must be a valid text.',
        'max_length': 'The model must be at least 50 characters long.',
    })
    color = serializers.CharField(max_length=50, required=True, error_messages={
        'required': 'The color is required.',
        'invalid': 'The color must be a valid text.',
        'max_length': 'The color must be at least 50 characters long.',
    })
    number = serializers.CharField(max_length=7, required=True, error_messages={
        'required': 'The number is required.',
        'invalid': 'The number must be a valid text.',
        'max_length': 'The number must be at least 7 characters long.',
    })
