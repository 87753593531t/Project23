from rest_framework import serializers

from people.models import City


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = (
            'uuid',
            'city',
            'author'
        )