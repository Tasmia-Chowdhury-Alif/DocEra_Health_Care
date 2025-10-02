"""
Serializers for Appointment model. Includes validations for time availability/fee, derived fields (doctor_fee, can_cancel).
"""
from rest_framework import serializers
from . import models
from doctor.models import Doctor, AvailableTime
from datetime import datetime, timedelta
from django.utils import timezone
from drf_spectacular.utils import extend_schema_serializer, OpenApiExample


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            'Online Appointment Create',
            value={'doctor': 1, 'time': 1, 'appointment_type': 'Online', 'symptom': 'Fever and cough'},
            description='Example for creating an online appointment.'
        ),
        OpenApiExample(
            'Offline Appointment Create',
            value={'doctor': 2, 'time': 3, 'appointment_type': 'Offline', 'symptom': 'Back pain'},
            description='Example for creating an offline appointment.'
        )
    ]
)
class AppointmentSerializer(serializers.ModelSerializer):
    """
    Serializer for Appointment model.
    
    Read-only fields for status/payment/created; validates doctor time/fee.
    Derived: doctor_fee (read-only), can_cancel (time/status-based).
    """
    patient = serializers.StringRelatedField()
    doctor = serializers.PrimaryKeyRelatedField(queryset=Doctor.objects.all())
    time = serializers.PrimaryKeyRelatedField(queryset=AvailableTime.objects.all())
    doctor_fee = serializers.SerializerMethodField()
    can_cancel = serializers.SerializerMethodField()

    class Meta:
        model = models.Appointment
        fields = "__all__"
        read_only_fields = ['appointment_status', 'payment_status', 'stripe_session_id', 'created_at', 'doctor_fee', 'can_cancel', 'cancel']

    def get_doctor_fee(self, obj):
        help_text = "Doctor's consultation fee"
        return obj.doctor.fee 
    
    def get_can_cancel(self, obj):
        # Cancel allowed if:
        # 1. Status is Pending (online) or Running (offline)
        # 2. Not already cancelled
        # 3. Within 24 hours of creation (optional, adjustable)
        if obj.cancel: # if already canceled then can't cancel 
            return False
        if obj.appointment_status not in ['Pending', 'Running']: 
            return False
        # Time-based restriction (e.g., cancel within 24h)
        time_window = obj.created_at + timedelta(hours=24)
        return timezone.now() <= time_window
    
    def validate(self, data):
        doctor = data.get('doctor')

        if not doctor and self.instance:
            doctor = self.instance.doctor
        
        time = data.get('time')

        if doctor and time and time not in doctor.available_time.all():
            raise serializers.ValidationError("Selected time is not available for this doctor.")
        if doctor and not doctor.fee:
            raise serializers.ValidationError("Appointments require a fee for this doctor.")
        return data

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        if instance.doctor.fee and instance.appointment_type == 'Online':
            rep['total_amount'] = instance.doctor.fee  # For frontend display
        return rep
