from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import CreateChanelView, DeleteChanelView, GetDataChanel

urlpatterns = [
    # Token olish uchun
    path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # Tokenni yangilash uchun
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]


urlpatterns += [
    path('create-chanel', CreateChanelView.as_view(), name='create_chanel'),
    path('delete-chanel/<int:pk>', DeleteChanelView.as_view(), name='delete_chanel'),
    path('get-data-chanel', GetDataChanel.as_view(), name='get_data_chanel'),
]