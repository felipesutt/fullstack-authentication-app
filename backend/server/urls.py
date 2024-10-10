from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("loginuser", views.login_user, name="login_user"),
]