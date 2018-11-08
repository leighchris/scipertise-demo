from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

# Create your models here.


class CustomUserManager(UserManager):
    pass

class CustomUser(AbstractUser):
    objects = CustomUserManager()
    position = models.CharField(max_length =50, null=True, default='')
    bio = models.CharField(max_length=300, null=True, default='')
    

    

   