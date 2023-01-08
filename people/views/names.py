from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend


from people.models import Name
from people.serializers import NameSerializer
from people.filters import NameFilter


class NameViewSet(ModelViewSet):
    serializer_class = NameSerializer
    permission_classes = [IsAuthenticated]
    queryset = Name.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = NameFilter

    def get_serializer_class(self):
        serializer_class = NameSerializer

        if self.action == 'create':
            serializer_class = NameSerializer
        elif self.action == 'update':
            serializer_class = NameSerializer
        #
        return serializer_class
