from django.shortcuts import render, redirect
from django.urls import path
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from app.models import Categories, Course

from django.contrib import messages
from app.email_backend import EmailBackend

def base(request):
    return render(request, "base.html")

def home(request):
    #categories = Categories.objects.all()
    categories = Categories.objects.all().order_by("id")[0:5]
    #courses = Course.objects.all().filter(status="Published").order_by("-id")[0:3]
    courses = Course.objects.all().filter(status="Published")
    
    context = {
        "categories": categories,
        "courses": courses
    }
    return render(request, "core/home.html", context)

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

        
        
def profile(request):
    return render(request, "registration/profile.html")

def profile_update(request):
    if request.method == "POST":
        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user_id = request.user.id

        user = User.objects.get(id=user_id)
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email

        if password != None and password != "":
            user.set_password(password)

        user.save()
        
        messages.success(request, "Profile updated successfully !")
        return redirect("profile")