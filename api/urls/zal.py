from django.urls import path

from api.views.zal import ZalRetrieveUpdateAPIView, ZalListAPIView

app_name = 'zal'

urlpatterns = [
    path('<int:id>/', ZalRetrieveUpdateAPIView.as_view(), name='zal-detail'),
    path('list/', ZalListAPIView.as_view(), name='zal-list')
]
