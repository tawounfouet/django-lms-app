from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("base", views.base, name="base"),
    path("", views.home, name="home"),
    path("course/single", views.course_single, name="course_single"),
    path("course/list", views.course_list, name="course_list"),
    path("contact", views.contact_us, name="contact_us"),
    path("about", views.about_us, name="about_us"),

    
]
