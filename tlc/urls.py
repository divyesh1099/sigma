from django.urls import path
from . import views
app_name="tlc"
urlpatterns=[
    path("", views.index, name="index"),
    path("newarticle", views.newarticle, name="newarticle"),
]