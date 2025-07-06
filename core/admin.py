from django.contrib import admin
from .models import CustomUser, BusinessProfile
from django.contrib.auth.admin import UserAdmin

class BusinessProfileAdmin(admin.ModelAdmin):
    list_display = ('business_name', 'user')
    readonly_fields = ('user',)  # ✅ prevents changing user
    # OR use exclude = ['user'] if you want to hide it instead

admin.site.register(CustomUser, UserAdmin)
admin.site.register(BusinessProfile, BusinessProfileAdmin)
