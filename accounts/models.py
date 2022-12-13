from django.contrib.auth.models import AbstractUser
from django.db import models

from accounts.managers import UserManager


class User(AbstractUser):
    username = models.CharField(max_length=30, blank=True, unique=True, null=True, default="")
  
    
    age = models.IntegerField(blank=True, null=True, default="1")
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    def __unicode__(self):
        return self.username

    objects = UserManager()
