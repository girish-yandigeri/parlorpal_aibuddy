from django.contrib import admin

# Register your models here.
from django.contrib import admin  # ✅ CORRECT

from .models import CustomUser, BusinessProfile

admin.site.register(CustomUser)
admin.site.register(BusinessProfile)
