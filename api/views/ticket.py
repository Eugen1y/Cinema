from rest_framework.generics import *

from api.permisions import UserAPIPermission, UserListAPIPermission
from api.serializers import TicketSerializer
from ticket.models import Ticket


class TicketListAPIView(ListCreateAPIView):
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()
    permission_classes = [UserListAPIPermission]


class TicketRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    lookup_field = 'id'
    permission_classes = [UserListAPIPermission]