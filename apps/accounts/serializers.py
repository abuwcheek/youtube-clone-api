from rest_framework import serializers

from .models import Chanel



class ChanelSerializers(serializers.ModelSerializer):
     followers_count = serializers.SerializerMethodField()
     class Meta:
          model = Chanel
          fields = [ 'id', 'user', 'name', 'icon', 'banner', 'description', 'followers_count']


     def get_followers_count(self, obj):
          return obj.followers.all().count()



class ChanelDataForVideoSerializers(serializers.ModelSerializer):
     user = serializers.HiddenField(default=serializers.CurrentUserDefault())
     is_followed = serializers.SerializerMethodField()
     followers_count = serializers.SerializerMethodField()
     
     class Meta:
          model = Chanel
          fields = [ 'id', 'user', 'name', 'icon', 'is_followed', 'followers_count']


     def get_is_followed(self, obj):
          user = self.context.get('request').user
          return user in obj.followers.all()

     @staticmethod
     def get_followers_count(obj):
          return obj.followers.all().count()