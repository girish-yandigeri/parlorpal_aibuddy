from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Extra fields if needed later
    pass

class BusinessProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)  # Keep cascade here ✅
    business_name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='uploads/', null=True, blank=True)

    def __str__(self):
        return self.business_name or f"Profile of {self.user.username}"
