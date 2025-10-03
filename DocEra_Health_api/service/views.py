from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from drf_spectacular.utils import extend_schema_view, extend_schema

# Create your views here.
@extend_schema_view(
    list=extend_schema(tags=['service'], description='List services.'),
    create=extend_schema(tags=['service'], description='Create service (admin).'),
    retrieve=extend_schema(tags=['service'], description='Get service details.'),
    update=extend_schema(tags=['service'], description='Update service (admin).'),
    destroy=extend_schema(tags=['service'], description='Delete service (admin).')
)
class ServiceViewset(viewsets.ModelViewSet):
    """
    ViewSet for Service CRUD.
    """
    queryset = models.Service.objects.all()
    serializer_class = serializers.ServiceSerializer