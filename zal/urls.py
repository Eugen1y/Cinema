from django.urls import path

from zal.views import ZalCreate, ZalList, SeansCreate, SeansList, FilmAdd, FilmList

appname = 'zal'
urlpatterns = [
    path('zal/create/', ZalCreate.as_view(), name='zal-create'),
    path('zals/', ZalList.as_view(), name='zal-list'),
    path('seans/create/', SeansCreate.as_view(), name='seans-create'),
    path('seans/list', SeansList.as_view(), name='seans-list'),
    path('film/add/', FilmAdd.as_view(), name='film-add'),
    path('film/list', FilmList.as_view(), name='film-list'),
]
