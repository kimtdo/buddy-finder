from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView # <--
from . import views
from . views import ProfileView, ReportView
from .views import filter_view

app_name = "social_app"
urlpatterns = [
    path('', TemplateView.as_view(template_name="social_app/index.html")), # <--
    path('profile/', ProfileView.as_view(), name="profile"),
    path('filter/', filter_view, name="filter"),
    path('reportuser/', ReportView.as_view(), name="report"),
    path('reported/', TemplateView.as_view(template_name="social_app/done_report.html")),
]