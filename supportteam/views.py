from django.shortcuts import redirect, render
from django.contrib.auth.models import Permission, User
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def index(request):
    if request.user.is_authenticated:
        return render(request, "home.html")
    else:
        return render(request, "login.html")


def login_user(request):
    username = request.POST["email"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(index)
    else:
        return render(request, "error.html", {"message": "Not a valid user"})


def logout_user(request):
    logout(request)
    return redirect(index)


def register_user(request):
    pass
