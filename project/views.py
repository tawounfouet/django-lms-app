from django.shortcuts import render, redirect
from django.urls import path

def base(request):
    return render(request, "base.html")