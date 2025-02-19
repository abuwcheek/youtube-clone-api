from rest_framework.serializers import ModelSerializer

from .models import Video, View, Like, Comment, CommentLike



class VideoSerializers(ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'