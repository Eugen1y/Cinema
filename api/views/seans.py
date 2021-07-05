from rest_framework.generics import *

from api.permisions import UserAPIPermission, UserListAPIPermission
from api.serializers import SeansSerializer
from zal.models import Seans


class SeansListAPIView(ListCreateAPIView):
    serializer_class = SeansSerializer
    queryset = Seans.objects.all()
    permission_classes = [UserListAPIPermission]


class SeansRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Seans.objects.all()
    serializer_class = SeansSerializer
    lookup_field = 'id'
    permission_classes = [UserListAPIPermission]
