from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import ChanelSerializers



class CreateChanel(APIView):
     def post(self, request):
          chanel = request.user.chanel
          if chanel:
               data = {
                    'status': False,
                    'message': 'Bu userda kanal mavjud'
               }
               return Response(data=data)