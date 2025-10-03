"""
Custom permissions for role-based access.
"""
from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Allows read-only access to all users and full access to admin users (is_staff=True).
    """

    def has_permission(self, request, view):
        # Allow safe methods (GET, HEAD, OPTIONS) for all
        if request.method in permissions.SAFE_METHODS:
            return True
        # Allow write methods (POST, PUT, DELETE) only for admins
        return request.user and request.user.is_staff


class IsPatientOrAdmin(permissions.BasePermission):
    """
    Object-level permission: Own patient or admin.
    """
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return obj.patient.user == request.user
    

class IsPatientOrAdminForReviews(permissions.BasePermission):
    """
    For reviews: Patients can create, admins full access, read-only others.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.method == 'POST':
            return request.user.is_authenticated and request.user.profile.role == 'patient'
        return request.user.is_authenticated and request.user.is_staff