from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
# Create your models here.
interest = (('item_key1', 'Item title 1.1'),
            ('item_key2', 'Item title 1.2'),
            ('item_key3', 'Item title 1.3'),
            ('item_key4', 'Item title 1.4'),
            ('item_key5', 'Item title 1.5'))

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=1000, null=True, blank=True)
    gender = models.CharField(max_length=140, null=True, blank=True) 
    profile_pic =  models.ImageField(upload_to='images', default="def.jpg", null=True, blank=True)
    interests = MultiSelectField(null=True,choices=interest)
    isReported = models.BooleanField(default=False)