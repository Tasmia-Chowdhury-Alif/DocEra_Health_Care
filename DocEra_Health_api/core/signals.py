"""Signals for automatic profile creation on User/Doctor save. Creates profiles, handles role switches, group assignments.
"""
import logging
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, Group

from .models import UserProfile
from patient.models import Patient
from doctor.models import Doctor

logger = logging.getLogger(__name__)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Create a UserProfile for new users and handle patient profile creation.
    - Superusers get role='admin'.
    - Non-superusers get role='patient' and a Patient profile.
    """

    if created:
        if instance.is_superuser:
            UserProfile.objects.create(user=instance, role="admin")
        else:
            UserProfile.objects.create(user=instance, role="patient")
            Patient.objects.create(user=instance)


@receiver(post_save, sender=Doctor)
@transaction.atomic
def update_user_role_to_doctor(sender, instance, created, **kwargs):
    """
    when a Doctor profile is created:
        - Deletes any existing Patient profile to enforce exclusive role assignment.
        - Updates the UserProfile role to 'doctor'.
        - Sets user.is_staff to True for admin panel access.
        - Adds the user to the 'Doctors' group for permission-based access control.
    Uses transaction.atomic to ensure all operations complete successfully or roll back.
    """
    if created:
        # Safely delete Patient profile if it exists
        try:
            patient_profile = Patient.objects.get(user=instance.user)
            patient_profile.delete()
        except Patient.DoesNotExist:
            pass

        try:
            user_profile = instance.user.profile
            user_profile.role = "doctor"
            user_profile.save()

        except UserProfile.DoesNotExist:
            # Handle case where UserProfile doesn't exist
            UserProfile.objects.create(user=instance.user, role="doctor")

        # Set user as staff for admin access and other staff-only features
        instance.user.is_staff = True
        instance.user.save(update_fields=["is_staff"])

        try:
            # Automatically add user to 'Doctors' group ( this Group is created Manually from admin panel ) for permission-based access control
            doctors_group = Group.objects.get(name="Doctors")
            instance.user.groups.add(doctors_group)
        except Group.DoesNotExist:
            logger.warning(
                "Doctors group not found. Create it in admin for permission enforcement."
            )
