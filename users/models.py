from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, verbose_name='telephone')
    date_of_birth = models.DateField(null=True, blank=True, verbose_name='date of birth')
    bio = models.TextField(max_length=500, blank=True, verbose_name='bio')
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name='img')

    def __str__(self):
        return f"{self.username} ({self.email})"

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
