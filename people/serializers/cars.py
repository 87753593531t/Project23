from rest_framework import serializers


from people.models import Car
from users.serializers import UserSerializer


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = (
            'uuid',
            'model',
            'number'
        )

