from rest_framework import serializers


from people.models import Name


class NameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Name
        fields = (
            'uuid',
            'name',
            'first_name',
            'cars',
            'city'
        )