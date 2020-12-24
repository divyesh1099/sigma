from django.shortcuts import render
from .models import *
from society.models import *
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
# Create your views here.
def index(request):
    try:
        posts=Post.objects.all()
        return render(request, "tlc/index.html", {
            "posts":posts
        })
    except:
        return render(request, "tlc/index.html")

def newarticle(request, userid):
    user=User.objects.get(pk=userid)
    if request.method=="POST":
        user=user
        title=request.POST["title"]
        content=request.POST["content"]
        try:
            post=Post(user=user, title=title, content=content)
            post.save()
        except IntegrityError:
            return render(request, "tlc/newarticle.html", {
                "message":"Article with that name Already Exists",
                "post.title":title,
                "post.content":content
            })
        login(request, user)
        return HttpResponseRedirect(reverse("tlc:index"), {
            "message": "The Post Was Created Successfuly"
        })
    else:
        return render(request, "tlc/newarticle.html")

def editarticle(request, userid, postname):
    user=User.objects.get(pk=userid)
    post=Post.objects.get(title=postname)
    print(post)
    if request.method=="POST":
        editedContent=request.POST["content"]
        editedTitle=request.POST["title"]
        try:
            post.title=editedTitle
            post.content=editedContent
            post.save()
        except IntegrityError:
            return render(request, "tlc/editarticle.html", {
                "message":"Article with the same name already Exists, either choose a different name or edit that article.",
                "user":user,
                "post":post
            })

        return HttpResponseRedirect(reverse("tlc:index"), {
        "message": "The Post Was Edited Successfuly"
        })
    else:
        print(post)
        return render(request, "tlc/editarticle.html", {
            "user": user,
            "post": post
        })