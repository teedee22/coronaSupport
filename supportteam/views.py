from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.conf import settings
from supportteam import airtable_api


import requests


# Create your views here.

sample_names = ['Skyler', 'Abi', 'Matt', 'Tim', 'Toby']


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


def register_page(request):
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

def scan_volunteer(request):
    max_records = 25

    # Call to Air Table
    # api_string = 'https://api.airtable.com/v0/apphZUrJD3wD17sah/Volunteers?maxRecords=' + str(max_records) +'&view=Volunteers%20master'
    # resp = requests.get(api_string, headers={'Authorization': 'Bearer ' + settings.AIRTABLE_API_KEY})
    # volunteers_full_json = resp.json()['records']

    # volunteer_names = []

    # for record in volunteers_full_json:
    #     volunteer_names.append(record.get('fields').get('Name'))

    # context = {
    #     "names" : volunteer_names
    # }
    volunteers = {}
    try:
        context = {
            "volunteers" : airtable_api.getVolunteersTable(),
            "status" : "Success",
            "message" : "Message test"
        }
    except:
        context = {
            "volunteers" : airtable_api.getVolunteersTable(),
            "status" : "Failed",
            "message" : "Connection with Airtable failed. Check API key"
        }

    return render(request, "scan-volunteer.html", context)

def scan_requests(request):
    return render(request, "scan-requests.html")

def assign_requests(request):
    return render(request, "assign-requests.html")

def handle_sms(request):
    return render(request, "handle-sms.html")