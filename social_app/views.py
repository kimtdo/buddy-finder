from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, FormView
from .models import *
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.forms import ModelForm


# Create your views here.
class ProfileView(ListView):
    model = Profile
    template_name = 'social_app/profile.html'

    def get_context_data(self, *args, **kwargs):
        exist = Profile.objects.filter(user=self.request.user).exists()
        profiles = Profile.objects.all()
        context = super(ProfileView, self).get_context_data(*args, **kwargs)
        context['exist'] = exist
        context['profiles'] = profiles
        # context['form'] = filterForm()
        return context

    def post(self, request, *args, **kwargs):
        if self.request.method == 'POST':
            n = self.request.POST.get('name')
            a = self.request.POST.get('gender')
            b = self.request.POST.get('bio')
            one = self.request.POST.get('i1')
            i = list()
            if (one == 'on'):
                i.append(1)
            two = self.request.POST.get('i2')
            if (two == 'on'):
                i.append(2)
            three = self.request.POST.get('i3')
            if (three == 'on'):
                i.append(3)
            four = self.request.POST.get('i4')
            if (four == 'on'):
                i.append(4)
            five = self.request.POST.get('i5')
            if (five == 'on'):
                i.append(5)
            d = self.request.FILES.get('img', False)
            if d:
                p = Profile(user=self.request.user, name=n, gender=a, bio=b, interests=i, profile_pic=d)
            else:
                p = Profile(user=self.request.user, name=n, gender=a, bio=b, interests=i)
            p.save()
            return HttpResponseRedirect("/profile/")


def filter_view(request):
    context = {}
    profiles = Profile.objects.all()
    context['profiles'] = profiles
    context['form'] = filterForm()
    if request.method == "POST":
        form = filterForm(request.POST)
        if form.is_valid():
            f = form.cleaned_data['filter']
            a = f[0]
            context['filter'] = a
    return render(request, "social_app/filter.html", context)


class ReportView(ListView):
    model = Report
    template_name = "social_app/report.html"

    def post(self, request, *args, **kwargs):
        if self.request.method == 'POST':
            u = self.request.POST.get('username')
            m = self.request.POST.get('message')
            print(m)
            r = Report(username=u, message=m)
            r.save()
            return HttpResponseRedirect("/reported/")

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
