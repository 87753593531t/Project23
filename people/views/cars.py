from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from people.models import Car
from people.serializers import CarSerializer
from people.filters import CarFilter


class CarViewSet(ModelViewSet):
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticated]
    queryset = Car.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CarFilter


    def get_serializer_class(self):
        serializer_class = CarSerializer

        if self.action == 'create':
            serializer_class = CarSerializer
        elif self.action == 'update':
            serializer_class = CarSerializer
        #
        return serializer_class