from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Video, View, Like, Comment, CommentLike, CommentReply, PlayList
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


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email']


class CommentSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Comment
        fields = ['id', 'video', 'comment', 'user']

    def create(self, validated_data):
        user = self.context.get('user')
        validated_data['user'] = user
        return super().create(validated_data)


# bu serializerdagi data ni qo'lda yuborish
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['user'] = instance.user.username
        return data



class UpdateCommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['comment']

    def update(self, instance, validated_data):
        instance.comment = validated_data.get('comment', instance.comment)
        instance.save()
        return instance



class CommentReplySerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = CommentReply
        fields = ['id', 'comment', 'reply', 'user']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['user'] = instance.user.username
        return data



class UpdateCommentReplySerializers(serializers.ModelSerializer):
    class Meta:
        model = CommentReply
        fields = ['reply']

    def update(self, instance, validated_data):
        instance.reply = validated_data.get('reply', instance.reply)
        instance.save()
        return instance



class CreatePlayListSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = PlayList
        fields = ['id', 'title', 'videos', 'user']