# core/models.py

from django.db import models

class CustomUser(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  # Hashed password

    def __str__(self):
        return self.username


class BusinessProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/', null=True, blank=True)

    def __str__(self):
        return self.business_name
