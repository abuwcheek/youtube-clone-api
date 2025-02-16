from django.db import models
from django.contrib.auth.models import User
from apps.base.models import BaseModel



class Chanel(BaseModel):
     name = models.CharField(max_length=255)
     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='chanel', null=True, blank=True)
     icon = models.ImageField(upload_to='chanel_icon/', null=True, blank=True)
     banner = models.ImageField(upload_to='chanel_banner/', null=True, blank=True)
     description = models.TextField()
     followers = models.ManyToManyField(User, related_name='followed_chanels', blank=True)

     class Meta:
          verbose_name = 'Chanel'
          verbose_name_plural = 'Chanels'

     
     def __str__(self):
          return self.name