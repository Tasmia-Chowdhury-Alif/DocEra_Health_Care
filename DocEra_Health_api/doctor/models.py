"""
Models for doctor management. Includes designations, specializations, available times, doctors (with bio/meet_link), reviews (with ratings).
"""
from django.db import models
from django.contrib.auth.models import User
from patient.models import Patient
from django.core.validators import URLValidator
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.
STAR_CHOICES = [
    ('⭐', '1'),
    ('⭐⭐', '2'),
    ('⭐⭐⭐', '3'),
    ('⭐⭐⭐⭐', '4'),
    ('⭐⭐⭐⭐⭐', '5'),
]


class Designation(models.Model):
    name = models.CharField(max_length= 30)
    slug = models.SlugField(max_length= 40, unique=True)

    def __str__(self):
        return self.name 
    
class Specialization(models.Model):
    name = models.CharField(max_length= 30)
    slug = models.SlugField(max_length= 40, unique=True)

    def __str__(self):
        return self.name 
    
class AvailableTime(models.Model):
    time = models.CharField(max_length= 100, unique=True)

    def __str__(self):
        return self.time
    
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor')
    image = models.ImageField(upload_to= "doctors/images/", null=True, blank=True)
    bio = CKEditor5Field(max_length=1000, null=True, blank=True, config_name='default')
    designation = models.ManyToManyField(Designation)
    specialization = models.ManyToManyField(Specialization)
    available_time = models.ManyToManyField(AvailableTime)
    fee = models.PositiveIntegerField(null=True, blank=True)
    meet_link = models.URLField(max_length= 300, validators=[URLValidator()], null=True, blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Review(models.Model):
    reviewer = models.ForeignKey(Patient, on_delete= models.CASCADE, related_name= 'reviews')
    doctor = models.ForeignKey(Doctor, on_delete= models.CASCADE, related_name= 'reviews')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    rating = models.CharField(choices= STAR_CHOICES, max_length=5)

    def __str__(self):
        return f"{self.id} Patient: {self.reviewer.user.username} ; Doctor: {self.doctor.user.username}"

