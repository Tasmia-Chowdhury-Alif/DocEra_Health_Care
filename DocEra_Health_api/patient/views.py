from django.shortcuts import render
from rest_framework import viewsets, status, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from . import models
from . import serializers
from core.permissions import IsPatientOrAdmin
from drf_spectacular.utils import extend_schema
from drf_spectacular.utils import extend_schema_view


@extend_schema_view(
    list=extend_schema(tags=['patient'], description='List profiles (own for users, all for admins).'),
    create=extend_schema(tags=['patient'], description='Create Patient profile (auto via signals).'),
    retrieve=extend_schema(tags=['patient'], description='Get profile.'),
    update=extend_schema(tags=['patient'], description='Update own profile.'),
    destroy=extend_schema(tags=['patient'], description='Delete profile (admin).')
)
@extend_schema(
    summary="Manage patient profiles",
    description="Allows authenticated users to view or manage patient profiles. Non-admin users can only access their own profile.",
)
class PatientViewset(viewsets.ModelViewSet):
    """
    ViewSet for Patient CRUD.
    Queryset: Own for users, all for staff.
    """
    queryset = models.Patient.objects.all()
    serializer_class = serializers.PatientSerializer
    permission_classes = [IsAuthenticated, IsPatientOrAdmin]

    # only admin users can access all patient objects. others can only access their own object
    def get_queryset(self):
        if self.request.user.is_staff:
            return models.Patient.objects.all()
        return models.Patient.objects.filter(user=self.request.user)
