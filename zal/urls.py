from django.urls import path

from zal.views import ZalCreate, ZalList

appname = 'zal'
urlpatterns = [
    path('zal/create/', ZalCreate.as_view(), name='zal-create'),
    path('zals/', ZalList.as_view(), name='zal-list'),
]
