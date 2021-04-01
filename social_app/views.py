from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, FormView
from .models import *
from django.views import generic
from social_app.models import Profile


# Create your views here.
class ProfileView(generic.ListView):
    model = Profile
    template_name = 'social_app/profile.html'

    def get_context_data(self, *args, **kwargs):
        exist = Profile.objects.filter(user=self.request.user).exists()
        context = super(ProfileView, self).get_context_data(*args, **kwargs)
        context['exist'] = exist
        return context


def profile_view(request):
    context = {}

    a = Profile.objects.filter(user=request.user).exists()

    form = ProfileForm(request.POST)
    if form.is_valid():
        data = Profile()
        data.name = form.cleaned_data['name']
        data.bio = form.cleaned_data['bio']
        data.gender = form.cleaned_data['gender']
        data.interests = form.cleaned_data['interests']
        form.save()

    context = {'form': form}
    context['exist'] = a
    if (a == True):
        b = Profile.objects.values_list('isReported', flat=True).get(user_id=a)
        if (b == True):
            context['reported'] = b
    return render(request, "social_app/profile.html", context)


def display_view(request):
    context = {}
    return render(request, "social_app/display.html", context)
