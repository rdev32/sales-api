from django.db import models
from django.contrib.auth.models import AbstractUser

class Costumer(AbstractUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=100, default='noemail@found.com')
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

