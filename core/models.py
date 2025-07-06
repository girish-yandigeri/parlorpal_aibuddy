from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):  # ✅ Inherit from AbstractUser
    # You can add extra fields here in the future
    pass

class BusinessProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/', null=True, blank=True)

    def __str__(self):
        return self.business_name
