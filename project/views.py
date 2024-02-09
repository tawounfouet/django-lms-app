from django.shortcuts import render, redirect
from django.urls import path

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