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
          data = request.POST.copy()
          data['user'] = request.user.id
          serializer = ChanelSerializers(data=data)
          serializer.is_valid(raise_exception=True)
          serializer.save()
          response_data = {
               'status': True,
               'message': 'Kanal yaratildi',
               'data': serializer.data
          }
          return Response(data=data)


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