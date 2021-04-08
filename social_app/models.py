from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from django import forms
# Create your models here.
interest = ((1, 'Sports'),
            (2, 'Music'),
            (3, 'Movies'),
            (4, 'Cooking'),
            (5, 'Reading'),
            (0, ''))
i_choices = ((1, 'Sports'),
            (2, 'Music'),
            (3, 'Movies'),
            (4, 'Cooking'),
            (5, 'Reading'))
class filterForm(forms.Form):
    filter = forms.MultipleChoiceField(choices=i_choices)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=140, null=True, blank=True) 
    bio = models.CharField(max_length=1000, null=True, blank=True)
    gender = models.CharField(max_length=140, null=True, blank=True) 
    profile_pic = models.ImageField(upload_to='images', default="default.webp", null=True, blank=True)
    interests = MultiSelectField(null=True,choices=interest)
    #ifilter = filterForm()
    isReported = models.BooleanField(default=False)

class Report(models.Model):
    username = models.CharField(max_length=140, null=True, blank=True) 
    message = models.CharField(max_length=1000, null=True, blank=True)