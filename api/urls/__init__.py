from django.urls import path, include

app_name = 'api'

urlpatterns = [
    path('zal/', include('api.urls.zal', namespace='zal'), name='zal'),
    path('film/', include('api.urls.film', namespace='film'), name='film'),
    path('seans/', include('api.urls.seans', namespace='seans'), name='seans'),
    path('ticket/', include('api.urls.ticket', namespace='ticket'), name='ticket'),

]
