from rest_framework.permissions import BasePermission


class IsAdminUser(BasePermission):
    """
    Allows access only to admin users.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser   


class IsStaffUser(BasePermission):
    """
    Allows access only to staff/internal users.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_staff