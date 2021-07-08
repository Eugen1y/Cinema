from django.urls import path

from zal.views import ZalCreate, ZalList, SeansCreate, SeansList, FilmAdd, FilmList, SeansUpdate, SeansDetail, \
    ZalUpdate, ZalDetail

appname = 'zal'
urlpatterns = [
    path('zal/create/', ZalCreate.as_view(), name='zal-create'),
    path('zal/update/<int:pk>/', ZalUpdate.as_view(), name='zal-update'),
    path('zal/list', ZalList.as_view(), name='zal-list'),
    path('zal/detail/<int:pk>/', ZalDetail.as_view(), name='zal-detail'),
    path('seans/create/', SeansCreate.as_view(), name='seans-create'),
    path('seans/list', SeansList.as_view(), name='seans-list'),
    path('seans/<int:pk>/', SeansDetail.as_view(), name='seans-detail'),
    path('seans/update/<int:pk>/', SeansUpdate.as_view(), name='seans-update'),
    path('film/add/', FilmAdd.as_view(), name='film-add'),
    path('film/list/', FilmList.as_view(), name='film-list'),
]
