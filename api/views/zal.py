from rest_framework.generics import *

from api.serializers import ZalSerializer
from zal.models import Zal


class ZalListAPIView(ListAPIView):
    serializer_class = ZalSerializer
    queryset = Zal.objects.all()


class ZalRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Zal.objects.all()
    serializer_class = ZalSerializer
