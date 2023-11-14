from django.shortcuts import render, redirect
from imaplib import _Authenticator
from . forms import CreateUserForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import auth

def login_home(request):
    return render(request, 'home-page-login.html')

def employee_home(request):
    return render(request, 'homePageEmployee.html')

def profile(request): 
    return render(request, 'staticUserProfile.html')

def login(request):
    form = LoginForm()
    
    if request.method =='POST':
        
        form = LoginForm(request, data=request.POST)
        
        if form.is_valid():
            
            username = request.POST.get('username')
            
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                
                auth.login(request, user)
                
            return redirect("home")
        
    context = { 'form': form}
    return render(request, 'loginPage.html', context=context)

def register(request):
   
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("login")

    context = {"form": form}

    return render(request, "register.html", context=context)

def timeOffForm(request):
    return render(request, "timeOffRequestForm.html")

def forgotPass(request):
    return render(request, "forgotPass.html")