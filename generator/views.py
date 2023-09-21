from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as auth_logout
from .models import Passwords
from .forms import PasswordEntryForm
from django.contrib.auth.models import User
from django.contrib import messages
import string
import random


thepassword = ""
# Create your views here.


def home(request):
    active_tab = "password_generator"
    return render(request, "index.html", {"active_tab": active_tab})


def password(request):
    has_numbers = True if request.GET.get("has_numbers") == "on" else None
    has_special_chars = True if request.GET.get(
        "has_special_chars") == "on" else None
    length = int(request.GET.get("length"))
    thepassword = generatePass(length, has_numbers, has_special_chars)

    password_entry = Passwords(
        password=thepassword,
        date=timezone.now(),
        website="",
        login="",
        isSaved=False,
        user = request.user
    )
    password_entry.save()
    return render(request, "password.html", {"password": thepassword})


def about(request):
    active_tab = "about"
    return render(request, "about.html", {"active_tab": active_tab})

@login_required
def history(request):
    user = request.user
    user_passwords = Passwords.objects.filter(user = user, isSaved = False)
    active_tab = "history"
    return render(request, "history.html", {"passwords": user_passwords[::-1], "active_tab": active_tab})


def save_pass(request):
    if request.method == "POST":
        form = PasswordEntryForm(request.POST)
        if form.is_valid(): 
            user_login = form.cleaned_data["login"]
            user_password = form.cleaned_data["password"]
            user_website = form.cleaned_data["website"]
            date = timezone.now()
            existing_password = Passwords.objects.filter(password=password).first()
            if existing_password:
                existing_password.password = user_password
                existing_password.login = user_login
                existing_password.date = date
                existing_password.website = user_website
                existing_password.isSaved = True
                existing_password.save()

            else:
                password_entry = Passwords(
                        password=user_password,
                        date=date,
                        website=user_website,
                        login=user_login,
                        isSaved=True,
                        user=request.user
                    )
                password_entry.save()
            return redirect("saved_passwords")
    else:
        form = PasswordEntryForm()
    return render(request, "save_pass.html", {"form": form})


def saved_passwords(request):
    user = request.user
    saved_passwords = Passwords.objects.filter(user=user,isSaved=True)
    active_tab = "saved_passwords"
    return render(request, "saved_passwords.html", {"saved_passwords": saved_passwords[::-1], "active_tab": active_tab})


def register(request):
    active_tab = "register"
    thepassword = generatePass(16, True, True)
    if request.method == "POST":
        first_name = request.POST.get("firstName")
        last_name = request.POST.get("lastName")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username:
            try:
                user = User.objects.create_user(
                    username=username, password=password, first_name=first_name, last_name=last_name, email=email)
                user.save()
            except IntegrityError:
                messages.error(
                    request, "Пользователь с таким именем уже существует.")

    return render(request, "register.html", {"active_tab": active_tab, "password": thepassword})


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/user_profile")
        else:
            messages.error(
                request, "Неправильное имя пользователя или пароль.")
    active_tab = 'login'
    return render(request, "user_login.html", {"active_tab": active_tab})


def user_profile(request):
    return render(request, "user_profile.html")

def logout(request):
    if request.method == "GET":
        auth_logout(request)
    return redirect("user_login")

def generatePass(symbols_number, ifIntegers=None, ifSpecSymbols=None):
    password = ""
    ascii = string.ascii_letters
    ascii += string.digits if ifIntegers else ""
    ascii += string.punctuation if ifSpecSymbols else ""
    password = "".join(random.choice(ascii) for _ in range(symbols_number))
    return password
