from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import DestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Video
from .permissions import IsHasChanel
from .serializers import VideoSerializers
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


class DeleteVideoAPIView(DestroyAPIView):
     permission_classes = [IsAuthenticated]
     serializer_class = VideoSerializers
     queryset = Video.objects.filter(is_active=True)
     lookup_field = 'id'