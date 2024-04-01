from django.contrib.auth.models import AbstractUser
from django.db import models

class Golfer(AbstractUser):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    index = models.FloatField(default=18.0)
