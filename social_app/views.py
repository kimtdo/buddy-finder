from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView,CreateView,FormView
from .models import *
from django.views import generic

# Create your views here.
class ProfileView(generic.ListView):
    model = Profile
    template_name = 'social_app/profile.html'
    def get_context_data(self,*args,**kwargs):
        user_profile = Profile.objects.filter(user=self.request.user)
        context = {
            'user_profile': user_profile,
        }
        return context