from django.urls import path
from . import views
app_name="tlc"
urlpatterns=[
    path("", views.index, name="index"),
    path("newarticle/<str:userid>", views.newarticle, name="newarticle"),
    path("editarticle/<str:userid>/<str:postname>", views.editarticle, name="editarticle"),
    path("deletearticle/<str:userid>/<str:postname>", views.deletearticle, name="deletearticle"),
    path("<str:article>", views.article, name="article"),
]