from rest_framework import serializers

from .models import Chanel



class ChanelSerializers(serializers.ModelSerializer):
     followers_count = serializers.SerializerMethodField()
     class Meta:
          model = Chanel
          fields = [ 'id', 'user', 'name', 'icon', 'banner', 'description', 'followers_count']


     def get_followers_count(self, obj):
          return obj.followers.all().count()