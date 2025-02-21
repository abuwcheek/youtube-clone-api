from django.urls import path
from .views import CreateVideoAPIView, DeleteVideoView , UpdateVideoView, RetrieveVideoView, ListVideoView, LikeToVideoView

urlpatterns = [
     path('create-video', CreateVideoAPIView.as_view(), name='create-video'),
     path('delete-video/<int:pk>', DeleteVideoView.as_view(), name='delete-video'),
     path('update-video/<int:pk>', UpdateVideoView.as_view(), name='update-video'),
     path('retrieve-video/<int:pk>', RetrieveVideoView.as_view(), name='retrieve-video'),
     path('list-videos', ListVideoView.as_view(), name='list-video'),
     path('like-video', LikeToVideoView.as_view(), name='like-video')
]