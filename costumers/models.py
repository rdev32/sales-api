from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

class Manager(BaseUserManager):
    def create_user(self, username, password, **extra_fields):
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        user = self.create_user(username, password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

class Costumer(AbstractUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=100, default='noemail@found.com')
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    
    objects = Manager()
