from rest_framework.generics import *

from api.serializers import SeansSerializer
from zal.models import Seans


class SeansListAPIView(ListCreateAPIView):
    serializer_class = SeansSerializer
    queryset = Seans.objects.all()

    def post(self, request, *args, **kwargs):
        ...


class SeansRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Seans.objects.all()
    serializer_class = SeansSerializer


class SeansCreateAPIView(CreateAPIView):
    ...