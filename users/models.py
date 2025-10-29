from tabnanny import verbose
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    first_name = models.CharField(max_lenght=150, verbose_name='name')
    last_name = models.CharField(max_lenght=150, verbose_name='last name')
    phone = models.CharField(max_lenght=20, blank=True, verbose_name='telephone')
    date = models.DateField(null=True, blank=True, verbose_name='date of birth')
    bio = models.TextField(max_lengh=500, blank=True, null=True, verbose_name='bio')
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name='img')

    def

