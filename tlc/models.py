from django.db import models
from society.models import *
# Create your models here.
class Post(models.Model):
    user=models.ForeignKey(User, related_name="userofpost", on_delete=models.CASCADE)
    title=models.CharField(max_length=1000, unique=True)
    content=models.TextField()
    def __str__(self):
        return self.title