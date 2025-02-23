from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import DestroyAPIView, UpdateAPIView, RetrieveAPIView, ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import IsHasChanel, IsOwner, IsAuthor
from .models import Video, Like, Comment, CommentLike, CommentReply, PlayList
from .serializers import (VideoSerializers, CommentSerializers, 
                         UpdateCommentSerializers, CommentReplySerializers, 
                         UpdateCommentReplySerializers, CommentListSerializers,
                          CreatePlayListSerializers,)
from .paginations import MyPageNumberPagination
from apps.accounts.models import Chanel
from apps.accounts.serializers import ChanelDataForVideoSerializers
# Create your views here.



class CreateVideoAPIView(APIView):
     permission_classes = [IsAuthenticated, IsHasChanel]
     serializer_class = VideoSerializers

     def post(self, request):
          serializer = self.serializer_class(data=request.data)
          serializer.is_valid(raise_exception=True)
          video = serializer.save()
          chanel = request.user.chanel
          video.author = chanel
          video.save()

          data = {
               'status': True,
               'msg': 'Video yaratildi',
               'data': self.serializer_class(instance=video, context={'request': request}).data
          }
          return Response(data=data)


class DeleteVideoView(DestroyAPIView):
     permission_classes = [IsHasChanel, IsOwner]
     serializer_class = VideoSerializers
     queryset = Video.objects.filter(is_active=True)

     def destroy(self, request, *args, **kwargs):
          super().destroy(request, *args, **kwargs)
          data = {
               'status': True,
               'msg': 'Video o`chirildi'
          }
          return Response(data=data)



class UpdateVideoView(UpdateAPIView):
     permission_classes = [IsHasChanel, IsOwner]
     serializer_class = VideoSerializers
     queryset = Video.objects.filter(is_active=True)

     def update(self, request, *args, **kwargs):
          super().update(request, *args, **kwargs)
          data = {
               'status': True,
               'msg': 'Video o`zgartirildi'
          }
          return Response(data=data)



class RetrieveVideoView(RetrieveAPIView):
     permission_classes = [AllowAny]
     serializer_class = VideoSerializers
     queryset = Video.objects.all()



class ListVideoView(ListAPIView):
     permission_classes = [AllowAny]
     serializer_class = VideoSerializers
     queryset = Video.objects.filter(is_active=True)
     pagination_class = MyPageNumberPagination



class LikeToVideoView(APIView):
     permission_classes = [IsAuthenticated]
     
     def post(self, request):
          video = get_object_or_404(Video, id=request.data['video'])
          like = Like.objects.filter(video=video, user=request.user).first()
          dislike = request.data.get('dislike') == 'true'
          if like:     
               if like.dislike == dislike:
                    like.delete()
                    data = {
                         'status': True,
                         'msg': "like o'chirildi"
                    }
               else:
                    like.dislike = dislike
                    like.save()
                    data = {
                         'status': True,
                         'msg': "like o'zgartirildi"
                    }
          else:
               Like.objects.create(video=video, user=request.user, dislike=dislike)
               data = {
                    'status': True,
                    'msg': 'like bosildi'
               }
          return Response(data=data)



class CommentToVideoView(CreateAPIView):
     permission_classes = [IsAuthenticated]
     serializer_class = CommentSerializers
     queryset = Comment.objects.all()

     def get_serializer_context(self):
          context = super().get_serializer_context()
          context['user'] = self.request.user
          return context



class DeleteCommentVideoView(DestroyAPIView):
     permission_classes = [IsAuthenticated, IsAuthor]
     serializer_class = CommentSerializers
     queryset = Comment.objects.filter(is_active=True)

     def destroy(self, request, *args, **kwargs):
          super().destroy(request, *args, **kwargs)
          data = {
               'status': True,
               'msg': 'Comment o`chirildi'
          }
          return Response(data=data)



class UpdateCommentView(UpdateAPIView):
     permission_classes = [IsAuthenticated, IsAuthor]
     serializer_class = UpdateCommentSerializers
     queryset = Comment.objects.filter(is_active=True)

     def update(self, request, *args, **kwargs):
          super().update(request, *args, **kwargs)
          data = {
               'status': True,
               'msg': 'Comment o`zgartirildi'
          }
          return Response(data=data)



class LikeToCommentView(APIView):
     permission_classes = [IsAuthenticated]

     def post(self, request):
          comment = get_object_or_404(Comment, id=request.data['comment'])
          like = CommentLike.objects.filter(comment=comment, user=request.user).first()
          dislike = request.data.get('dislike') == 'true'
          if like:
               if like.dislike == dislike:
                    like.delete()
                    data = {
                         'status': True,
                         'msg': "like o'chirildi"
                    }
               else:
                    like.dislike = dislike
                    like.save()
                    data = {
                         'status': True,
                         'msg': "like o'zgartirildi"
                    }
          else:
               CommentLike.objects.create(comment=comment, user=request.user, dislike=dislike)
               data = {
                    'status': True,
                    'msg': 'like bosildi'
               }
          return  Response(data=data)



class CommentReplyView(CreateAPIView):
     permission_classes = [IsAuthenticated]
     serializer_class = CommentReplySerializers
     queryset = CommentReply.objects.all()



class DeleteCommentReplyView(DestroyAPIView):
     permission_classes = [IsAuthenticated, IsAuthor]
     serializer_class = CommentReplySerializers
     queryset = CommentReply.objects.filter(is_active=True)

     def destroy(self, request, *args, **kwargs):
          super().destroy(request, *args, **kwargs)
          data = {
               'status': True,
               'msg': 'Comment reply o`chirildi'
          }
          return Response(data=data)



class UpdateCommentReplyView(UpdateAPIView):
     permission_classes = [IsAuthenticated, IsAuthor]
     serializer_class = UpdateCommentReplySerializers
     queryset = CommentReply.objects.filter(is_active=True)

     def update(self, request, *args, **kwargs):
          super().update(request, *args, **kwargs)
          data = {
               'status': True,
               'msg': 'Comment reply o`zgartirildi'
          }
          return Response(data=data)



class CreatePlayListView(CreateAPIView):
     permission_classes = [IsAuthenticated]
     serializer_class = CreatePlayListSerializers
     queryset = PlayList.objects.all()



class DeletePlayListView(DestroyAPIView):
     permission_classes = [IsAuthenticated, IsAuthor]
     serializer_class = CreatePlayListSerializers
     queryset = PlayList.objects.filter(is_active=True)

     def destroy(self, request, *args, **kwargs):
          super().destroy(request, *args, **kwargs)
          data = {
               'status': True,
               'msg': 'PlayList o`chirildi'
          }
          return Response(data=data)



class AddVideoPlayListView(APIView):
     permission_classes = [IsAuthenticated]

     def post(self, request, pk):
          video = get_object_or_404(Video, id=request.data['video'])
          playlist = get_object_or_404(PlayList, id=pk)
          if request.user == playlist.user:
               playlist.videos.add(video)
               data = {
                    'status': True,
                    'msg': 'Video playlistga qo`shildi'
               }
          else:
               data = {
                    'status': False,
                    'msg': 'Siz playlist muallifi emassiz'
               }
          return Response(data=data)



class RemoveVideoFromPlayListView(APIView):
     permission_classes = [IsAuthenticated]

     def post(self, request, pk):
          video = get_object_or_404(Video, id=request.data['video'])
          playlist = get_object_or_404(PlayList, id=pk)
          if request.user == playlist.user:
               playlist.videos.remove(video)
               data = {
                    'status': True,
                    'msg': 'Video playlistdan o`chirildi'
               }
          else:
               data = {
                    'status': False,
                    'msg': 'Siz playlist muallifi emassiz'
               }
          return Response(data=data)



class FollowToChanelView(APIView):
     permission_classes = [IsAuthenticated]

     def post(self, request):
          chanel = get_object_or_404(Chanel, id=request.data['chanel'])
          user = request.user

          if user in chanel.followers.all():
               chanel.followers.remove(user)
               data = {
                    'status': True,
                    'msg': 'Obuna bekor qilindi'
               }
          else:
               chanel.followers.add(user)
               data = {
                    'status': True,
                    'msg': 'Obuna qilindi'
               }
          return Response(data=data)



class FollowedChanelsListView(ListAPIView):
     permission_classes = [IsAuthenticated]
     serializer_class = ChanelDataForVideoSerializers

     # (queryset) bilan (get_queryset) ni umuman farqi yoq 
     # oddiy-oddiy ishlaga masalan(is_active, filter) la uchun (queryset) mukammalroq ishla uchun masalan(user)ni tutib olish ili bashqa ishla uchun (get_queryset) ni ishlatish kerak 
     def get_queryset(self):
          user = self.request.user
          chanels = user.followed_chanels
          return chanels



class VideoCommentListView(ListAPIView):
     permission_classes = [AllowAny]
     serializer_class = CommentListSerializers
     queryset = Comment.objects.filter(is_active=True)

     def get_queryset(self):
          id = self.kwargs.get('pk')
          video = get_object_or_404(Video, id=id)
          comments = video.comments.filter(is_active=True)
          return comments