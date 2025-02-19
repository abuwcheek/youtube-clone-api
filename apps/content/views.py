from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Content
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import IsHasChanel
from .serializers import VideoSerializers
# Create your views here.



class CreateVideo(APIView):
     permission_classes = [IsAuthenticated, IsHasChanel]
     serializer_class = VideoSerializers

     def post(self, request):
          pass