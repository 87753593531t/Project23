from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend

from people.models import City
from people.serializers import CitySerializer
from people.filters import CityFilter


class CityViewSet(ModelViewSet):
    serializer_class = CitySerializer
    permission_classes = [IsAuthenticated]
    queryset = City.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CityFilter

    def get_serializer_class(self):
        serializer_class = CitySerializer

        if self.action == 'create':
            serializer_class = CitySerializer
        elif self.action == 'update':
            serializer_class = CitySerializer
        #
        return serializer_class
