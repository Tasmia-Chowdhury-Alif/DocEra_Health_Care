from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Service

# Register your models here.
admin.site.register(Service, ModelAdmin)