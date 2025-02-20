from rest_framework import serializers

from .models import Video, View, Like, Comment, CommentLike
from apps.accounts.serializers import ChanelSerializers


class VideoSerializers(serializers.ModelSerializer):

    chanel_name = serializers.SerializerMethodField()
    class Meta:
        model = Video
        fields = ['id', 'title', 'description', 'photo', 'video', 'category', 'author', 'chanel_name']


    # @staticmethod emas self bilan yozganimizni boisi chanelni rasm videolari (http) siz qolib ketti 
    # self tashqaridan malumotlarni oladi va context orqali ularga murojat qiladi, @staticmethod da bular ishlamaydi
    def get_chanel_name(self, obj):
        return ChanelSerializers(instance=obj.author, context={'request': self.context.get('request')}).data
