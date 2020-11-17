from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    phone = models.CharField(max_length=11)

    def __str__(self):
        # Article object (1) / username
        return f'User object ({self.pk})'