from django.urls import path
from . import views
app_name="crew5678"
urlpatterns=[
    path("", views.index, name="index"),
]