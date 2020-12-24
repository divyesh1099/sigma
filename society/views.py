from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import *
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def index(request):
    return render(request, "society/index.html")

def profile(request, userid):
    user=User.objects.get(pk=userid)
    if request.method == "POST":
        user=user
        bio=request.POST["bio"]
        dob=request.POST["dob"]
        pic=request.FILES.get('pic', False)
        try:
            profile=Profile(user=user, bio=bio, dob=dob, pic=pic)
            profile.save()
        except IntegrityError:
            return render(request, "society/profile.html", {
                "message": "THERE'S AN INTEGRITY ERROR",
                "user":user
            })
        login(request, user)
        return HttpResponseRedirect(reverse("society:index"))
    else:
        login(request, user)
        try:
            profile=Profile.objects.get(pk=userid)
        except ObjectDoesNotExist:
            profile=""
        return render(request, "society/profile.html", {
            "user":user,
            "profile":profile
        })

    

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("society:index"))
        else:
            return render(request, "society/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "society/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("society:index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "society/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.set_password(password)
            user.is_active=True
            user.save()
        except IntegrityError:
            return render(request, "society/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("society:index"))
    else:
        return render(request, "society/register.html")