from django.urls import path

from api.views.seans import SeansRetrieveUpdateAPIView, SeansListAPIView


app_name = 'seans'

urlpatterns = [
    path('<int:id>/', SeansRetrieveUpdateAPIView.as_view(), name='seans-detail'),
    path('list/', SeansListAPIView.as_view(), name='seans-list')
]
