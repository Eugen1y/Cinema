from django.urls import path

from api.views.film import FilmRetrieveUpdateAPIView, FilmListAPIView


app_name = 'film'

urlpatterns = [
    path('<int:pk>/', FilmRetrieveUpdateAPIView.as_view(), name='film-detail'),
    path('list/', FilmListAPIView.as_view(), name='film-list')
]
