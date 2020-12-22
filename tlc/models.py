from django.db import models
from society.models import *
# Create your models here.
class Post(models.Model):
    user=models.OneToOneField(User, related_name="userofpost", on_delete=models.CASCADE)
    title=models.CharField(max_length=1000)
    content=models.TextField()