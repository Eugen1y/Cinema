from django.urls import path

from api.views.user import UserRetrieveUpdateAPIView, UserListAPIView

app_name = 'user'

urlpatterns = [
    path('<int:id>/', UserRetrieveUpdateAPIView.as_view(), name='user-detail'),
    path('list/', UserListAPIView.as_view(), name='user-list')
]
