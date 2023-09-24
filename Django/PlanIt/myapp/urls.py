from django.urls import path
from . import views
import pyrebase

urlpatterns = [
    path("", views.home, name="home"),
    path("", views.index, name="index"),
]
