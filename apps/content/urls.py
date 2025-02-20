from django.urls import path
from .views import CreateVideoAPIView

urlpatterns = [
     path('create-video', CreateVideoAPIView.as_view(), name='create-video'),
]