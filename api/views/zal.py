from rest_framework.generics import *

from api.permisions import UserListAPIPermission
from api.serializers import ZalSerializer
from zal.models import Zal


class ZalListAPIView(ListCreateAPIView):
    serializer_class = ZalSerializer
    queryset = Zal.objects.all()
    permission_classes = [UserListAPIPermission]


class ZalRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Zal.objects.all()
    serializer_class = ZalSerializer
    lookup_field = 'id'
    permission_classes = [UserListAPIPermission]
