from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import DestroyAPIView, UpdateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import IsHasChanel, IsOwner
from .models import Video
from .serializers import VideoSerializers
from .paginations import MyPageNumberPagination
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