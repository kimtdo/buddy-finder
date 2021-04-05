from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
# Create your models here.
interest = ((1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (0, ''))

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=140, null=True, blank=True) 
    bio = models.CharField(max_length=1000, null=True, blank=True)
    gender = models.CharField(max_length=140, null=True, blank=True) 
    profile_pic = models.ImageField(upload_to='images', default="def.jpg", null=True, blank=True)
    interests = MultiSelectField(null=True,choices=interest)
    # isReported = models.BooleanField(default=False)