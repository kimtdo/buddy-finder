from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView,CreateView,FormView
from .models import *
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.forms import ModelForm

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
            n = self.request.POST.get('name')
            a = self.request.POST.get('gender')
            b = self.request.POST.get('bio')
            one = self.request.POST.get('i1')
            o=0
            tw=0
            th=0
            fo=0
            fi=0
            i = list()
            if(one=='on'):
                o=1
                i.append(o)
            two = self.request.POST.get('i2')
            if (two == 'on'):
                tw=2
                i.append(tw)
            three = self.request.POST.get('i3')
            if (three == 'on'):
                th=3
                i.append(th)
            four = self.request.POST.get('i4')
            if (four == 'on'):
                fo = 4
                i.append(fo)
            five = self.request.POST.get('i5')
            if (five == 'on'):
                fi = 5
                i.append(fi)
            d = self.request.FILES.get('img', False)
            if d:
                p = Profile(user=self.request.user, name=n, gender=a, bio=b, interests=i, profile_pic=d)
            else:
                p = Profile(user=self.request.user, name=n, gender=a, bio=b, interests=i)
            p.save()
            return HttpResponseRedirect("/profile/")

# class ThoughtForm(ModelForm):
#     class Meta:
#         model = Message
#         fields = ['title', 'body']
#         widgets = {
#             'title': forms.TextInput(
#                 attrs={
#                     'class': 'form-control'}),
#             'body': forms.Textarea(
#                 attrs={
#                     'class': 'form-control'}),
#             }
#
# class ThoughtCreate(CreateView):
#     model = Message
#     form_class = ThoughtForm