from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Patient

# Register your models here.
class PatientModelAdmin(ModelAdmin):
    list_display = ['first_name', 'last_name', 'mobile_no', 'image']

    def first_name(self, obj):
        return obj.user.first_name
    def last_name(self, obj):
        return obj.user.last_name

admin.site.register(Patient, PatientModelAdmin)