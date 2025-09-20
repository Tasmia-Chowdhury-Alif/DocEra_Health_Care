from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Doctor, Designation, Specialization, AvailableTime, Review

# Register your models here.
class DesignationAdmin(ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class SpecializationAdmin(ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Doctor, ModelAdmin)
admin.site.register(Designation, DesignationAdmin)
admin.site.register(Specialization, SpecializationAdmin)
admin.site.register(AvailableTime, ModelAdmin)
admin.site.register(Review, ModelAdmin)