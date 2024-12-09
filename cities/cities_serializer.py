from rest_framework import serializers


class CitiesSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50, error_messages={
        'invalid': 'The name must be a valid text.',
        'max_length': 'The name must be at least 50 characters long.',
    })
    usage = serializers.IntegerField(
        error_messages={
            'invalid': 'The usage must be a valid integer.',
        }
    )

    def to_representation(self, instance):
        result = super(CitiesSerializer, self).to_representation(instance)
        data = {
            instance.id: {
                'id': instance.id,
                'name': result['name'],
                'usage': result['usage'],
            }
        }
        return data


class CitySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50, error_messages={
        'invalid': 'The name must be a valid text.',
        'max_length': 'The name must be at least 50 characters long.',
    })