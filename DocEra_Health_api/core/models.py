"""Core models for user profiles and roles."""
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    """
    Profile extension for User, defining roles (patient/doctor/admin).
    
    Created via signals on User/Doctor save.
    """
    ROLE_CHOICES = (
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
        ('admin', 'Admin'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='patient', db_index=True)

    def __str__(self):
        return f"{self.user.username} - {self.role}"