from rest_framework import serializers


class CarSerializer(serializers.Serializer):
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
            'model': result['model'],
            'color': result['color'],
            'number': result['number'],
        }
        return data
