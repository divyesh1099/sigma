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
            "posts":posts,
        })
    except:
        return render(request, "tlc/index.html", {
            "message":"SOME ERROR OCCURED",
            "type": "danger"
        })

def newarticle(request, userid):
    user=User.objects.get(pk=userid)
    if request.method=="POST":
        user=user
        title=request.POST["title"]
        thumbnail=request.FILES.get("thumbnail")
        content=request.POST["content"]
        if title:
            pass
        else:
            return render(request, "tlc/newarticle.html", {
                "message":"TITLE NOT PROVIDED",
            })
        if thumbnail:
            pass
        else:
            return render(request, "tlc/newarticle.html", {
                "message":"THUMBNAIL NOT PROVIDED",
            })
        if content:
            pass
        else:
            return render(request, "tlc/newarticle.html", {
                "message":"No Content",
            })
        try:
            post=Post(user=user, title=title, thumbnail=thumbnail, content=content)
            post.save()
        except IntegrityError:
            post={"title":title, "thumbnail":thumbnail, "content":content}
            return render(request, "tlc/newarticle.html", {
                "message":"Article with that name Already Exists",
                "post":post
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
    if request.method=="POST":
        editedContent=request.POST["content"]
        editedThumbnail=request.FILES.get('thumbnail')
        editedTitle=request.POST["title"]
        try:
            if editedTitle:
                post.title=editedTitle
            else:
                pass
            if editedThumbnail:
                post.thumbnail=editedThumbnail
            else:
                pass
            if editedContent:
                post.content=editedContent
            else:
                pass
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
        return render(request, "tlc/editarticle.html", {
            "user": user,
            "post": post
        })
    
def deletearticle(request, userid, postname):
    try:
        post=Post.objects.get(title=postname)
        post.delete()
        return HttpResponseRedirect(reverse("tlc:index"))
    except:
        return HttpResponseRedirect(reverse("tlc:index"))

def article(request, article):
    try:
        post=Post.objects.get(title=article)
        return render(request, "tlc/article.html", {
            "post":post
        })
    except:
        try:
            posts=Post.objects.all()
            return render(request, "tlc/index.html", {
                "message":"SOME ERROR OCCURED",
                "type": "danger",
                "posts":posts
            })
        except:
            return render(request, "tlc/index.html", {
                "message":"SOME ERROR OCCURED",
                "type": "danger"
            })
