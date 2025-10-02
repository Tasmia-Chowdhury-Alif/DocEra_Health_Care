from django.shortcuts import render
from rest_framework import viewsets
from . import models 
from . import serializers 
from drf_spectacular.utils import extend_schema_view, extend_schema

# Create your views here.
@extend_schema_view(
    list=extend_schema(tags=['contact_us'], description='List all contacts (admin only).'),
    create=extend_schema(tags=['contact_us'], description='Submit new contact inquiry.'),
    retrieve=extend_schema(tags=['contact_us'], description='Get contact details.'),
    update=extend_schema(tags=['contact_us'], description='Update contact (admin).'),
    destroy=extend_schema(tags=['contact_us'], description='Delete contact (admin).')
)
class ContactUsViewset(viewsets.ModelViewSet):
    """
    ViewSet for ContactUs CRUD.
    """
    queryset = models.ContactUs.objects.all()
    serializer_class = serializers.ContactUsSerializer