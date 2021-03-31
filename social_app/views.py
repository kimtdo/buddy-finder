from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView,CreateView,FormView
from .models import *
# from .forms import DeleteForm
from django.views import generic
from django.http import HttpResponse

# Create your views here.
class ProfileView(generic.ListView):
    model = Profile
    template_name = 'social_app/profile.html'
    # form_class=DeleteForm
    def get_context_data(self,*args,**kwargs):
        exist = Profile.objects.filter(user=self.request.user).exists()
        profiles = Profile.objects.all()
        context = super(ProfileView,self).get_context_data(*args,**kwargs)
        context['exist'] = exist
        context['profiles'] = profiles
        return context
    # def delete_user(self,form):
    #  if request.method == 'POST':
    #     form=DeleteForm(request.POST)
    #     if form.is_valid():
    #         deleted=form.request.POST['user']
    #         Profile.objects.get(user=deleted).delete()
    #         return HttpResponse('')
    #     else:
    #         form=DeleteForm()
    #     return render(request,'social_app/profile.html',{'form':form})
# def delete_user(request):
#      if request.method == 'POST':
#             deleted=request.POST.get('user')
#             Profile.objects.get(user=deleted).delete()
#             return HttpResponse('')



###Reading in profile info from form###
# def profiles(request):
#     if request.method=='POST':
#         a = request.POST.get('gender')
#         b = request.POST.get('bio')
#         c = request.POST.get('interests')
#         d = request.POST.get('img')
#         p = Profile(gender=a, bio=b, interests=c, profile_pic=d)
#         p.save()
#     return render(request, 'social_app/profile.html')

