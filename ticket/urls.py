from django.urls import path

from ticket.views import TicketDetail, TicketCreate, TicketList

appname = 'ticket'

urlpatterns = [
    path('ticket/<int:pk>/', TicketDetail.as_view(), name='ticket-detail'),
    path('ticket/list/', TicketList.as_view(), name='ticket-list'),
    path('ticket/create/', TicketCreate.as_view(), name='ticket-create'),
]
