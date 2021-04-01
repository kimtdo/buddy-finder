from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView,CreateView,FormView
from .models import *
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
class ProfileView(ListView):
    model = Profile
    template_name = 'social_app/profile.html'

    def get_context_data(self,*args,**kwargs):
        exist = Profile.objects.filter(user=self.request.user).exists()
        profiles = Profile.objects.all()
        context = super(ProfileView,self).get_context_data(*args,**kwargs)
        context['exist'] = exist
        context['profiles'] = profiles
        return context
    def post(self,request,*args,**kwargs):
        if self.request.method=='POST':
            a = self.request.POST.get('gender')
            b = self.request.POST.get('bio')
            c = self.request.POST.get('interests')
            d = self.request.POST.get('img')
            p = Profile(user=self.request.user,gender=a, bio=b, interests=c, profile_pic=d)
            p.save()
            return HttpResponseRedirect("")
