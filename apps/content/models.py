from django.db import models
from apps.accounts.models import User, Chanel
from apps.base.models import BaseModel


class Category(BaseModel):
     title = models.CharField(max_length=255)


     class Meta:
          verbose_name = 'Category'
          verbose_name_plural = 'Categories'

     
     def __str__(self):
          return self.title



class Video(BaseModel):
     title = models.CharField(max_length=255)
     description = models.TextField(null=True, blank=True)
     photo = models.ImageField(upload_to='videos/')
     video = models.FileField(upload_to='content_videos/')
     author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='content_videos', null=True, blank=True)
     category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='category_videos')

     class Meta:
          verbose_name = 'Content'
          verbose_name_plural = 'Contents'

     
     def __str__(self):
          return self.title



class View(BaseModel):
     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='views')
     video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='views')

     class Meta:
          verbose_name = 'View'
          verbose_name_plural = 'Views'

     
     def __str__(self):
          return f'{self.user.username} - {self.video.title}'



class Like(BaseModel):
     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
     video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='likes')
     dislike = models.BooleanField(default=False)

     class Meta:
          verbose_name = 'Like'
          verbose_name_plural = 'Likes'

     
     def __str__(self):
          return f'{self.user.username} - {self.video.title}'



class Comment(BaseModel):
     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
     video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='comments')
     comment = models.TextField()

     class Meta:
          verbose_name = 'Comment'
          verbose_name_plural = 'Comments'

     
     def __str__(self):
          return f'{self.user.username} - {self.video.title}'



class CommentLike(BaseModel):
     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_likes')
     comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='comment_likes')
     dislike = models.BooleanField(default=False)

     class Meta:
          verbose_name = 'Comment Like'
          verbose_name_plural = 'Comment Likes'

     
     def __str__(self):
          return f'{self.user.username} - {self.comment.comment}'



class CommentReply(BaseModel):
     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_replies')
     comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='comment_replies')
     reply = models.TextField()

     class Meta:
          verbose_name = 'Comment Reply'
          verbose_name_plural = 'Comment Replies'

     
     def __str__(self):
          return f'{self.user.username} - {self.comment.comment}'



class PlayList(BaseModel):
     author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_playlists')
     title = models.CharField(max_length=255)
     videos = models.ManyToManyField(Video, related_name='videos_playlists')