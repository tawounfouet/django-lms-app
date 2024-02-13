from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("base", views.base, name="base"),
    path("", views.home, name="home"),
    path("course/single", views.course_single, name="course_single"),
    path("course/list", views.course_list, name="course_list"),
    path("contact", views.contact_us, name="contact_us"),
    path("about", views.about_us, name="about_us"),

    # registration
    path("accounts/register/", views.register, name="register"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("doLogin", views.do_login, name="do_login"),
    path("accounts/profile", views.profile, name="profile"),
    path("accounts/profile/update", views.profile_update, name="profile_update"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
