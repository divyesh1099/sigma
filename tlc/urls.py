from django.urls import path
from . import views
app_name="tlc"
urlpatterns=[
    path("", views.index, name="index"),
    path("newarticle/<str:userid>", views.newarticle, name="newarticle"),
    path("editarticle/<str:userid>/<str:postname>", views.editarticle, name="editarticle"),
]