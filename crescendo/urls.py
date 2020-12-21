from django.urls import path
from . import views
app_name="crescendo"
urlpatterns=[
    path("", views.index, name="index"),
]