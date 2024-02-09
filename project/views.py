from django.shortcuts import render, redirect
from django.urls import path
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from app.email_backend import EmailBackend

def base(request):
    return render(request, "base.html")

def home(request):
    return render(request, "core/home.html")

def course_single(request):
    return render(request, "core/course_single.html")


def course_list(request):
    return render(request, "core/course_list.html")


def contact_us(request):
    return render(request, "core/contact_us.html")


def about_us(request):
    return render(request, "core/about_us.html")

# def login(request):
#     return render(request, "authentication/login.html")

def do_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        #print(email, password)
        
        user = EmailBackend.authenticate(request, username=email, password=password)
        # if user != None:
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Email or Password are Invalid !")
            return redirect("login")
        
    return render(request, "registration/login.html")


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        #print(username, email, password)

        # check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists !")
            return redirect("register")
        
        # check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists !")
            return redirect("register")
        
        # create user
        #user = User.objects.create_user(username=username, email=email, password=password)
        user = User(username=username, email=email)
        user.save()
        messages.success(request, "Account created successfully !")
        return redirect("login")
    
    return render(request, "registration/register.html")    

        
        





   