from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

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


def register(request):
    return render(request, "register.html")


def register_new_user(request):
    username = request.POST["email"]
    password = request.POST["password"]
    password2 = request.POST["password2"]

    if not password == password2:
        return render(
            request, "error.html", {"message": "passwords must match"}
        )
    try:
        validate_password(
            password=password, user=username, password_validators=None
        )
        print(password)
    except ValidationError as error:
        return render(request, "error.html", {"message": error})

    user = User.objects.create_user(username, username, password)
    user.save()
    user = authenticate(request, username=username, password=password)
    login(request, user)
    return redirect(index)
