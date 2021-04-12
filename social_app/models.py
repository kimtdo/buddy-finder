from datetime import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

# Create your models here.
interest = ((1, 'Sports'),
            (2, 'Music'),
            (3, 'Movies'),
            (4, 'Cooking'),
            (5, 'Reading'),
            (0, ''))


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=140, null=True, blank=True)
    bio = models.CharField(max_length=1000, null=True, blank=True)
    gender = models.CharField(max_length=140, null=True, blank=True)
    profile_pic = models.ImageField(upload_to='images', default="default.webp", null=True, blank=True)
    interests = MultiSelectField(null=True, choices=interest)

    # isReported = models.BooleanField(default=False)


class Message(models.Model):
    sender = models.ForeignKey(User, related_name="sender", on_delete=models.CASCADE)
    reciever = models.ForeignKey(User, related_name="recipient", on_delete=models.CASCADE)
    msg_content = models.CharField(max_length=10000)
    created_at = models.DateTimeField('time sent', default=datetime.now)
