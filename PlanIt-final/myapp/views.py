from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, ShiftAssignmentForm, UpdateUserForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import auth, User
from .models import Shift
from django.contrib import messages


def login_home(request):
    return render(request, "home-page-login.html")


def register(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

            # Log in the user after registration
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)
                return redirect("home")
            else:
                # Handle authentication failure if needed
                pass
    else:
        form = CreateUserForm()

    return render(request, "register.html", {"form": form})


@login_required
def employee_home(request):
    shifts = Shift.objects.all()

    return render(request, "homePageEmployee.html", {"shifts": shifts})


def profile(request):
    return render(request, "staticUserProfile.html")


def custom_login(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)

            return redirect("home")

    context = {"form": form}
    return render(request, "loginPage.html", context=context)


def timeOffForm(request):
    return render(request, "timeOffRequestForm.html")


def forgotPass(request):
    return render(request, "forgotPass.html")


@user_passes_test(lambda user: user.is_staff, login_url="home")
def shiftCreate(request):
    if request.method == "POST":
        form = ShiftAssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            print(form.errors)
    else:
        form = ShiftAssignmentForm()
    context = {"form": form}
    return render(request, "shiftCreate.html", context)


def profile_management(request):
    form = UpdateUserForm(instance=request.user)

    if request.method == "POST":
        form = UpdateUserForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()

            return redirect("home")

    context = {"ProfileForm": form}

    return render(request, "profile-management.html", context)


@login_required(login_url="my-login")
def delete_account(request):
    if request.method == "POST":
        deleteUser = User.objects.get(username=request.user)

        deleteUser.delete()

        return redirect("")

    return render(request, "delete-account.html")
