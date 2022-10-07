from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import CharField

# Create your models here.
class signup(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=50)
    