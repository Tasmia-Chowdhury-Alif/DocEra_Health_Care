from django.contrib import admin
from .models import Appointment

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.shortcuts import redirect

# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'doctor_username', 'patient_username', 'appointment_type', 'appointment_status', 'payment_status', 'symptom', 'time', 'cancel']
    search_fields = ['patient__user__username', 'doctor__user__username'] # Search on patient/doctor username
    list_filter = ['created_at', 'appointment_status', 'payment_status', 'time', 'doctor', 'cancel']  # Filters for date, status, doctor (visible only to superusers)
    date_hierarchy = 'created_at'  # Hierarchical date navigation

    def doctor_username(self, obj):
        return obj.doctor.user.username or 'N/A'

    def patient_username(self, obj):
        return obj.patient.user.username or 'N/A'
    
    def save_model(self, request, obj, form, change):
        if obj.appointment_type == "Online" and obj.appointment_status == "Running" :
            email_subject = "Your Online Appointment is Running"
            email_body = render_to_string('appointment/appointment_running_email.html', {"user" : obj.patient.user, "doctor" : obj.doctor})

            email = EmailMultiAlternatives(email_subject, '', to=[obj.patient.user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()
        return super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        """
            Overrides the default queryset to apply user-specific filtering.
            Ensures data isolation: doctors see only their appointments.
            Queryset: Filtered Appointment instances 
            (all for superusers, user-owned for doctors, empty otherwise).
        """

        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset  # Superusers can see everything
        if hasattr(request.user, 'doctor') and request.user.doctor:
            return queryset.filter(doctor=request.user.doctor)  # Filter to doctor's own appointments 
        return queryset.none()  # Non-doctors get no access (empty set)
    
    def get_readonly_fields(self, request, obj=None):
        """
        Define fields that should be read-only based on user permissions.
        For non-superusers:
            - All fields are read-only to prevent unauthorized edits (doctors can view but not edit).
        For superusers:
            - No fields are read-only (full control).
        """
        if request.user.is_superuser:
            return ()
        return ('patient', 'doctor', 'appointment_type', 'payment_status', 'stripe_session_id', 'payment_intent_id')
    
admin.site.register(Appointment, AppointmentAdmin)