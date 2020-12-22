from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.conf import settings
from django.contrib.auth import get_user_model as user_model
from tinymce.models import HTMLField
# Create your models here.
class User(AbstractUser):
    pass

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name="userofprofile")
    bio=models.TextField(max_length=500, help_text="Describe Yourself in 500 words or less", blank=True)
    dob=models.DateField(help_text="Date of Birth", blank=True)
    pic=models.ImageField(upload_to='images', blank=True)

    def __str__(self):
        return self.user.username