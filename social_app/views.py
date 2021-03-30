from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView,CreateView,FormView
from .models import *
from django.views import generic
from social_app.models import Profile


# Create your views here.
class ProfileView(generic.ListView):
    model = Profile
    template_name = 'social_app/profile.html'
    def get_context_data(self,*args,**kwargs):
        exist = Profile.objects.filter(user=self.request.user).exists()
        context = super(ProfileView,self).get_context_data(*args,**kwargs)
        context['exist'] = exist
        return context

def profile_view(request):
    context = {}
    form = ProfileForm(request.POST)

    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "social_app/profile.html", context)
