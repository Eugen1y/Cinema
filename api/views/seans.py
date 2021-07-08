from rest_framework.generics import *

from api.permisions import UserListAPIPermission
from api.serializers import SeansSerializer, SeansGroupSerializer
from zal.models import SeansGroup, Seans


class SeansListAPIView(ListCreateAPIView):
    serializer_class = SeansSerializer
    queryset = Seans.objects.all()
    permission_classes = [UserListAPIPermission]


class SeansRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Seans.objects.all()
    serializer_class = SeansSerializer
    lookup_field = 'id'
    permission_classes = [UserListAPIPermission]

class SeansGroupListAPIView(ListCreateAPIView):
    serializer_class = SeansGroupSerializer
    queryset = SeansGroup.objects.all()
    permission_classes = [UserListAPIPermission]


class SeansGroupRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = SeansGroup.objects.all()
    serializer_class = SeansGroupSerializer
    lookup_field = 'id'
    permission_classes = [UserListAPIPermission]

