from rest_framework.generics import *

from api.permisions import UserListAPIPermission, UserAPIPermission
from api.serializers import FilmSerializer
from zal.models import Film


class FilmListAPIView(ListCreateAPIView):
    serializer_class = FilmSerializer
    queryset = Film.objects.all()
    permission_classes = [UserListAPIPermission]


class FilmRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    lookup_field = 'id'
    permission_classes = [UserListAPIPermission]
