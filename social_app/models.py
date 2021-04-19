from datetime import datetime
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _
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
    interests = MultiSelectField(null=True, choices=interest)
    friends = models.ManyToManyField(User, related_name='f')
    # ifilter = filterForm()
    isReported = models.BooleanField(default=False)

#https://medium.com/analytics-vidhya/add-friends-with-689a2fa4e41d reference
class Friend_Request(models.Model):
    from_user = models.ForeignKey(User, related_name='from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='to_user', on_delete=models.CASCADE)


class Report(models.Model):
    username = models.CharField(max_length=140, null=True, blank=True)
    message = models.CharField(max_length=1000, null=True, blank=True)


class Message(models.Model):
    sender = models.ForeignKey(User, related_name="sender", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="recipient", on_delete=models.CASCADE)
    msg_content = models.CharField(max_length=10000)
    created_at = models.DateTimeField('time sent', default=datetime.now)
    isread = models.BooleanField(default=False)

    def clean(self):
        # Check if user has a profile
        if len(Profile.objects.filter(user=self.receiver)) == 0:
            raise ValidationError(_('Cannot message a user without a profile'))
