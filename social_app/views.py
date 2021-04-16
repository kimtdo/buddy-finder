from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, FormView
from .models import *
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.forms import ModelForm
from django.db.models import Q


# Create your views here.
def send_friend_request(request,userID):
    from_user = request.user
    to_user = User.objects.get(id=userID)
    friend_request, created = Friend_Request.objects.get_or_create(from_user=from_user,to_user=to_user)
    if created:
        return HttpResponse('Friend Request Sent')
    else:
        return HttpResponse('Friend Request Already Sent')

def accept_friend_request(request, requestID):
    friend_request = Friend_Request.objects.get(id=requestID)
    if friend_request.to_user == request.user:
        friend_request.to_user.profile.friends.add(friend_request.from_user)
        friend_request.from_user.profile.friends.add(friend_request.to_user)
        friend_request.delete()
        return HttpResponse('Friend Request Accepted')
    else:
        return HttpResponse('Friend Request Not Accepted')
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
        context['friend_requests']=Friend_Request.objects.all()
       # context['friends'] = Profile.objects.filter(user=self.request.user).values('friends')
        f = Profile.objects.filter(user=self.request.user).values('friends')
        friends = list()
        for i in f:
            friends.append(i['friends'])
        context['friends']=friends
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
    #print(profiles)
    context['profiles'] = profiles
    context['form'] = filterForm()
    p = Profile.objects.all().values('user_id')
    ids =list()
    for x in p:
        ids.append(x['user_id'])
    f = Profile.objects.filter(user=request.user).values('friends')
    friends = list()
    for i in f:
        friends.append(i['friends'])
    context['friends'] = friends
    not_friends =list()
    for d in ids:
        if friends.count(d) == 0:
            not_friends.append(d)
    context['not_friends'] = not_friends
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


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['msg_content', 'receiver']
        widgets = {
            'msg_content': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }),
            'receiver': forms.Select(
                attrs={
                    'class': 'form-control'
                }),
        }


class MessageCreate(CreateView):
    model = Message
    form_class = MessageForm
    initial = {'msg_content': 'test'}

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.sender = self.request.user
        rec = str(obj.receiver.pk)
        obj.save()
        return HttpResponseRedirect("/message/" + rec)


class MessageView(generic.ListView):
    model = Message
    template_name = 'social_app/messages.html'
    context_object_name = 'messages'

    def get_context_data(self, **kwargs):
        ctx = super(MessageView, self).get_context_data(**kwargs)
        ctx['title'] = 'My Messages with ' + Profile.objects.get(user=User.objects.get(pk=self.kwargs['rec_id'])).name
        ctx['me'] = self.request.user
        return ctx

    def get_queryset(self):
        me = self.request.user
        other = User.objects.get(pk=self.kwargs['rec_id'])
        return Message.objects.filter(
            Q(sender=me) | Q(sender=other), Q(receiver=me) | Q(receiver=other)
        ).order_by('created_at')


class AllMessageView(generic.ListView):
    model = Message
    template_name = 'social_app/messages.html'
    context_object_name = 'messages'
