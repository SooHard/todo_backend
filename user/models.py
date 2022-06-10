from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    country = models.CharField(max_length=20, blank=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
