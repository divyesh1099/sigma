from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "tlc/index.html")

def newarticle(request):
    return render(request, "tlc/newarticle.html")