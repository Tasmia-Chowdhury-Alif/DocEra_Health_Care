from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import UserProfile

# Register your models here.
admin.site.register(UserProfile, ModelAdmin)