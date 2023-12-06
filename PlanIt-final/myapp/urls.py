from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.login_home, name=""),
    path("home", views.employee_home, name="home"),
    path("profile", views.profile, name="profile"),
    path("login", views.custom_login, name="login"),
    path("register", views.register, name="register"),
    path("timeOffForm", views.timeOffForm, name="timeOffForm"),
    path("shiftCreate", views.shiftCreate, name="shiftCreate"),
    path("profile-management", views.profile_management, name="profile-management"),
    path("delete-account", views.delete_account, name="delete-account"),
    # password management
    # 1. allow us to enter our email to receive password
    path(
        "reset_password",
        auth_views.PasswordResetView.as_view(template_name="password-reset.html"),
        name="reset_password",
    ),
    # 2. show a success message theat the email was sent
    path(
        "reset_password_sent",
        auth_views.PasswordResetDoneView.as_view(
            template_name="password-reset-sent.html"
        ),
        name="password_reset_done",
    ),
    # 3. send link to email, so we can reset our password
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="password-reset-form.html"
        ),
        name="password_reset_confirm",
    ),
    # 4. show success message that password was changed
    path(
        "password_reset_complete",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="password-reset-complete.html"
        ),
        name="password_reset_complete",
    ),
]


# path("", views.index, name="index"),
