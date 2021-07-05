from django.urls import path

from api.views.ticket import TicketRetrieveUpdateAPIView, TicketListAPIView


app_name = 'ticket'

urlpatterns = [
    path('<int:id>/', TicketRetrieveUpdateAPIView.as_view(), name='ticket-detail'),
    path('list/', TicketListAPIView.as_view(), name='ticket-list')
]
