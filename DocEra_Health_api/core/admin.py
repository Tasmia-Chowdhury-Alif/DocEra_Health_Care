from django.contrib import admin
from .models import UserProfile

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    """
    Admin for UserProfile: displays role, user.
    """
    list_display = ('user', 'role')
    list_filter = ('role',)
    search_fields = ('user__username', 'role')

admin.site.register(UserProfile, UserProfileAdmin)