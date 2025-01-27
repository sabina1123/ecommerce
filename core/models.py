from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique = True)
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    
    objects = UserManager()
