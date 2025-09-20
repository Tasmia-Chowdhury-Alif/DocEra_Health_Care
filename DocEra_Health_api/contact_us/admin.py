from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import ContactUs

# Register your models here.
class ContactModelAdmin(ModelAdmin):
    list_display = ['name', 'phone', 'problem']
    
admin.site.register(ContactUs, ContactModelAdmin)