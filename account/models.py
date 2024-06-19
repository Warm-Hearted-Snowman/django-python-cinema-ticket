from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class Profile(AbstractUser):
    phone_number = models.CharField(max_length=15)
