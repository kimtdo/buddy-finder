from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView # <--
from . import views
from . views import ProfileView

app_name = "social_app"
urlpatterns = [
    path('', TemplateView.as_view(template_name="social_app/index.html")), # <--
    path('profile/', views.profile_view, name="profile"),
]