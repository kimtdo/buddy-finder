from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView # <--
from . import views
from . views import *

app_name = "social_app"
urlpatterns = [
    path('', TemplateView.as_view(template_name="social_app/index.html"), name='home'), # <--
    path('profile/', ProfileView.as_view(), name="profile"),
    path('filter/', filter_view, name="filter"),
    path('reportuser/', ReportView.as_view(), name="report"),
    path('reported/', TemplateView.as_view(template_name="social_app/done_report.html")),
    path('browse/', TemplateView.as_view(template_name="social_app/browsing.html")),
    path('edit/', EditProfileView.as_view(), name="edit_profile"),
    #path('message', AllMessageView.as_view(), name='all_messages'),
    path('inbox', AllMessageView.as_view(), name='inbox'),
    path('message/<int:rec_id>/', MessageView.as_view(), name='view_messages'),
    path('compose', MessageCreate.as_view(), name='compose'),
    path('compose/<int:rec_id>/', MessageCreateSpecific.as_view(), name='compose2'),
    path('send_friend_request/<int:userID>/',send_friend_request, name='send_friend_request'),
    path('accept_friend_request/<int:requestID>/',accept_friend_request,name='accept_friend_request'),
]