from rest_framework.generics import *

from api.serializers import FilmSerializer
from zal.models import Film


class FilmListAPIView(ListAPIView):
    serializer_class = FilmSerializer
    queryset = Film.objects.all()


class FilmRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
