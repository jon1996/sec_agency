from django.contrib import admin
from django.urls import path
from .views import article_form, user_login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", article_form, name="home"),
    #path("login/", user_login, name="login"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", auth_views.logout_then_login, name="logout"),
]