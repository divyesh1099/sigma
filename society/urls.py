from django.urls import path
from . import views
app_name="society"
urlpatterns=[
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("login", views.login_view, name="login"),
    path("profile/<str:userid>", views.profile, name="profile"),
    path("logout", views.logout_view, name="logout"),
]