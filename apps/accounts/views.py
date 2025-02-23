from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import ChanelSerializers
from .models import Chanel



class CreateChanelView(APIView):
     permission_classes = [IsAuthenticated]
     def post(self, request):
          try:
               chanel = request.user.chanel
               if chanel:
                    data = {
                         'status': False,
                         'message': 'Bu userda kanal mavjud'
                    }
                    return Response(data=data)
          except Exception as ex:
               pass

          serializer = ChanelSerializers(data=request.data, context={'request': request})
          serializer.is_valid(raise_exception=True)
          chanel = serializer.save()
          chanel.user = request.user
          chanel.save()
          response_data = {
               'status': True,
               'message': 'Kanal yaratildi',
               'data': serializer.data
          }
          return Response(data=response_data)


class DeleteChanelView(APIView):
     permission_classes = [IsAuthenticated]

     def delete(self, request, pk):
          chanel = get_object_or_404(Chanel, pk=pk)
          if chanel.user == request.user:
               chanel.delete()
               data = {
                    'satatus': True,
                    'message': "Kanal o'chirildi"
               }
               return Response(data=data)
          else:
               data = {
                    'status': False,
                    'message': 'Kanal sizga tegishli emas'
               }
               return Response(data=data)



class GetDataChanel(APIView):
     permission_classes = [IsAuthenticated]

     def get(self, request):
          chanel = request.user.chanel

          serializer = ChanelSerializers(instance=chanel, context={'request': request})
          data = {
               'status': True,
               'data': serializer.data
          }
          return Response(data=data)
          

