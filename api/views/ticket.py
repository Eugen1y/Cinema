from rest_framework.generics import *

from api.serializers import TicketSerializer
from ticket.models import Ticket


class TicketListAPIView(ListAPIView):
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()


class TicketRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
