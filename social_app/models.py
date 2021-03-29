from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=1000, null=True, blank=True)
    gender = models.CharField(max_length=140, null=True, blank=True) 
    profile_pic =  models.ImageField(upload_to='social_app/images', blank=True)
    isReported = models.BooleanField(default=False)

