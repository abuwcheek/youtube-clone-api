from rest_framework.serializers import ModelSerializer

from .models import Chanel



class ChanelSerializers(ModelSerializer):
     class Meta:
          model = Chanel
          fields = [ 'id', 'user', 'name', 'icon', 'banner', 'description']