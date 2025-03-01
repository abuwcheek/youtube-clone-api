from django.urls import path
from .views import (CreateVideoAPIView, DeleteVideoView, 
                    UpdateVideoView, RetrieveVideoView, 
                    ListVideoView, LikeToVideoView, 
                    CommentToVideoView, DeleteCommentVideoView,
                    UpdateCommentView, LikeToCommentView,
                    CommentReplyView, DeleteCommentReplyView,
                    UpdateCommentReplyView, CreatePlayListView,
                    DeletePlayListView, AddVideoPlayListView,
                    RemoveVideoFromPlayListView, FollowToChanelView,
                    FollowedChanelsListView, VideoCommentListView,
                    PlayListVideoView, PlayListRetrieveView,
                    LikedVideosView, CategoryListView, CategoryRetrieveView,
                    SearchVideosView, OrderByTime, OrderByLike, OrderByView)



from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
openapi.Info(
     title="My REST GROUP API",
     default_version='v1',
     description="API hujjatlari",
     terms_of_service="https://www.google.com/policies/terms/",
     contact=openapi.Contact(email="abdulloistamov1034@gmail.com"),
     license=openapi.License(name="BSD License"),
),
public=True,
permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]



urlpatterns += [
     path('create-video', CreateVideoAPIView.as_view(), name='create-video'),
     path('delete-video/<int:pk>', DeleteVideoView.as_view(), name='delete-video'),
     path('update-video/<int:pk>', UpdateVideoView.as_view(), name='update-video'),
     path('retrieve-video/<int:pk>', RetrieveVideoView.as_view(), name='retrieve-video'),
     path('list-videos', ListVideoView.as_view(), name='list-video'),
     path('like-video', LikeToVideoView.as_view(), name='like-video'),
     path('comment-video', CommentToVideoView.as_view(), name='comment-video'),
     path('delete-comment/<int:pk>', DeleteCommentVideoView.as_view(), name='delete-comment'),
     path('update-comment/<int:pk>', UpdateCommentView.as_view(), name='update-comment'),
     path('like-comment', LikeToCommentView.as_view(), name='like-comment'),
     path('comment-reply', CommentReplyView.as_view(), name='comment-reply'),
     path('delete-comment-reply/<int:pk>', DeleteCommentReplyView.as_view(), name='delete-comment-reply'),
     path('update-comment-reply/<int:pk>', UpdateCommentReplyView.as_view(), name='update-comment-reply'),
     path('create-playlist', CreatePlayListView.as_view(), name='create-playlist'),
     path('delete-playlist/<int:pk>', DeletePlayListView.as_view(), name='delete-playlist'),
     path('add-video-playlist/<int:pk>', AddVideoPlayListView.as_view(), name='add-video-playlist'),
     path('remove-video-playlist/<int:pk>', RemoveVideoFromPlayListView.as_view(), name='remove-video-playlist'),
     path('follow-to-chanel', FollowToChanelView.as_view(), name='follow-chanel'),
     path('followed-chanels', FollowedChanelsListView.as_view(), name='followed-chanels'),
     path('video-comments/<int:pk>', VideoCommentListView.as_view(), name='video-comments'),
     path('playlist-list', PlayListVideoView.as_view(), name='playlistlist'),
     path('playlist-retrieve/<int:pk>', PlayListRetrieveView.as_view(), name='playlistretrieve'),
     path('liked-videos', LikedVideosView.as_view(), name='liked-videos'),
     path('category-list', CategoryListView.as_view(), name='category-list'),
     path('category-retrieve/<int:pk>', CategoryRetrieveView.as_view(), name='category-retrieve'),
     path('search-videos/<str:search>', SearchVideosView.as_view(), name='search-videos'),
     path('order-by-time', OrderByTime.as_view(), name='order-by-time'),
     path('order-by-like', OrderByLike.as_view(), name='order-by-like'),
     path('order-by-view', OrderByView.as_view(), name='order-by-view'),
]