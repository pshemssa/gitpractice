from django.contrib import admin
from django.urls import path
from pelin import views

urlpatterns = [
    path("", views.home, name="home"),
]
