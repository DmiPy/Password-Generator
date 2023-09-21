"""
URL configuration for password_generator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from generator import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home),
    path("password/", views.password, name="password"),
    path("about/", views.about),
    path("history/", views.history, name = "history"),
    path("save_pass/", views.save_pass, name = "save_pass"),
    path("saved_passwords/", views.saved_passwords, name = "saved_passwords"),
    path("register/", views.register, name = "register"),
    path("user_login/", views.user_login, name = "user_login"),
    path("user_profile/", views.user_profile, name = "user_profile"),
    path("logout/", views.logout, name = "logout")
]
