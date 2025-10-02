from rest_framework import serializers
from . import models 
from drf_spectacular.utils import extend_schema_serializer


@extend_schema_serializer()
class ServiceSerializer(serializers.ModelSerializer):
    """
    Serializer for Service CRUD.
    """
    class Meta:
        model = models.Service
        fields = '__all__'
        extra_kwargs = {'description': {'help_text': 'Rich text (CKEditor).'}}