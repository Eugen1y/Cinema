from django.contrib.auth.models import User
from rest_framework.generics import *

from api.permisions import UserAPIPermission, UserListAPIPermission
from api.serializers import UserSerializer


class UserListAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserListAPIPermission]


class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'id'
    permission_classes = [UserAPIPermission]
