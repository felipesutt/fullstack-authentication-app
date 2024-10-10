from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("loginuser", views.login_user, name="login_user"),
    path("fingerprint", views.digital_authentication, name="fingerprint"),
    path("facial", views.facial_authentication, name="fingerprint"),
    path("getinfo", views.get_information, name="fingerprint"),
]