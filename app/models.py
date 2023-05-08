from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime

class user(models.Model):
    profile_picture = models.ImageField(upload_to='profile_picture/',blank=True,null=True)
    phone_number = models.CharField(max_length=20,blank=True, null=True)
    
class author(models.Model):
    user = models.OneToOneField(get_user_model(),on_delete=models.CASCADE)
    
class TimeStampedModel(models.Model):
    create_timestamp = models.DateTimeField(auto_now_add=True)
    update_timestamp = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(author,on_delete=models.SET_NULL,null=True,blank=True)
    
    class Meta:
        abstract = True
        
class Blog(TimeStampedModel):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(default = datetime.now, blank=True)
    
class Comment(TimeStampedModel):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
