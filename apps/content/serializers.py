from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Video, View, Like, Comment, CommentLike, CommentReply, PlayList, Category
from apps.accounts.serializers import ChanelSerializers, ChanelDataForVideoSerializers


class VideoSerializers(serializers.ModelSerializer):
    chanel_name = serializers.SerializerMethodField()
    views = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Video
        fields = ['id', 'title', 'description', 'photo', 'video', 'created_at', 'views', 'category', 'author', 'chanel_name', 'likes_count']


    # @staticmethod emas self bilan yozganimizni boisi chanelni rasm videolari (http) siz qolib ketti 
    # self tashqaridan malumotlarni oladi va context orqali ularga murojat qiladi, @staticmethod da bular ishlamaydi
    def get_chanel_name(self, obj):
        return ChanelDataForVideoSerializers(instance=obj.author, context={'request': self.context.get('request')}).data

    def get_views(self, obj):
        return obj.views.count()


    def get_likes_count(self, obj):
        user = self.context.get('request').user.id
        like = Like.objects.filter(user=user, dislike=False)
        dislike = Like.objects.filter(user=user, dislike=True)
        is_liked = like.exists()
        is_disliked = dislike.exists()
        data = {
            'is_liked': is_liked,
            'is_disliked': is_disliked,
            'likes': obj.likes.filter(dislike=False).count(),
            'dislikes': obj.likes.filter(dislike=True).count(),
        }
        return data


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



class CommentListSerializers(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()
    comment_replies = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = ['id', 'comment', 'user', 'likes_count', 'comment_replies']

    def get_likes_count(self, obj):
        user = self.context.get('request').user
        like = CommentLike.objects.filter(user=user, comment=obj, dislike=False)
        dislike = CommentLike.objects.filter(user=user, comment=obj, dislike=True)
        is_liked = like.exists()
        is_disliked = dislike.exists()
        data = {
            'is_liked': is_liked,
            'is_disliked': is_disliked,
            'likes': obj.comment_likes.filter(dislike=False).count(),
            'dislikes': obj.comment_likes.filter(dislike=True).count(),
        }
        return data


    def get_comment_replies(self, obj):
        comments = obj.comment_replies.all()
        return CommentReplySerializers(instance=comments, many=True).data



class CreatePlayListSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = PlayList
        fields = ['id', 'title', 'videos', 'user']



class PlayListVideoSerializers(serializers.ModelSerializer):
    videos_count = serializers.SerializerMethodField()
    class Meta:
        model = PlayList
        fields = ['id' ,'user', 'videos_count', 'title']


    @staticmethod
    def get_videos_count(obj):
        return obj.videos.count()



class PlayListSerializers(serializers.ModelSerializer):
    videos = serializers.SerializerMethodField()
    class Meta:
        model = PlayList
        fields = ['title', 'user', 'videos']

    
    @staticmethod
    def get_videos(obj):
        vds = obj.videos
        return VideoListSerializers(instance=vds, many=True).data   



class VideoListSerializers(serializers.ModelSerializer):
    chanel = serializers.SerializerMethodField()
    views_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Video
        fields = ['title', 'author', 'photo', 'chanel', 'views_count', 'created_at']


    @staticmethod
    def get_chanel(obj):
        return obj.author.name

    @staticmethod
    def get_views_count(obj):
        return obj.views.count()



class CategorySerializers(serializers.ModelSerializer):
    ctg_videos = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = ['name', 'ctg_videos']

    @staticmethod
    def get_ctg_videos(obj):
        ctg_vds = ctg_vds.category_videos
        return VideoListSerializers(instance=ctg_vds, many=True).data 



class CategoryListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id' ,'name']
