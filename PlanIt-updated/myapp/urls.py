from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.login_home, name=""),
    path("home", views.employee_home, name="home"),
    path('profile', views.profile, name='profile'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('timeOffForm', views.timeOffForm, name='timeOffForm'),
    path('forgotPass', views.forgotPass, name= 'forgotPass'),
    path('shiftCreate', views.shiftCreate, name= 'shiftCreate'),

    # path("", views.index, name="index"),
] 