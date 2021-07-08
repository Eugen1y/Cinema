from django.urls import path

from api.views.seans import SeansRetrieveUpdateAPIView, SeansListAPIView, SeansGroupRetrieveUpdateAPIView, \
    SeansGroupListAPIView

app_name = 'seans'

urlpatterns = [
    path('<int:id>/', SeansRetrieveUpdateAPIView.as_view(), name='seans-detail'),
    path('list/', SeansListAPIView.as_view(), name='seans-list'),
    path('group/<int:id>/', SeansGroupRetrieveUpdateAPIView.as_view(), name='seans-group-detail'),
    path('group/list/', SeansGroupListAPIView.as_view(), name='seans-group-list'),
]
