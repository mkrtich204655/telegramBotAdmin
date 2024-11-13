from rest_framework import serializers


class RideSerializer(serializers.Serializer):
    from_city_id = serializers.IntegerField(required=True, error_messages={
        'required': 'The City ID field is required.',
        'invalid': 'The City ID must be a valid integer.'
    }
                                            )
    to_city_id = serializers.IntegerField(required=True, error_messages={
        'required': 'The City ID field is required.',
        'invalid': 'The City ID must be a valid integer.'
    }
                                          )
    user_id = serializers.IntegerField(required=True, error_messages={
        'required': 'The User ID field is required.',
        'invalid': 'The User ID must be a valid integer.'
    }
                                       )
    car_id = serializers.IntegerField(required=True, error_messages={
        'required': 'The Car ID field is required.',
        'invalid': 'The Car ID must be a valid integer.'
    }
                                      )
    price = serializers.IntegerField(error_messages={
        'invalid': 'The Price must be a valid integer.'
    })
    places = serializers.IntegerField(error_messages={
        'invalid': 'The Places must be a valid integer.'
    })
    free_places = serializers.IntegerField(error_messages={
        'invalid': 'The Free Places must be a valid integer.'
    })
    date = serializers.DateField(error_messages={
        'invalid': 'The Date must be a valid date.'
    })
    time = serializers.TimeField(error_messages={
        'invalid': 'The Time must be a valid time.'
    })
    baggage = serializers.BooleanField(error_messages={
        'invalid': 'The Baggage must be a valid boolean.'
    })
