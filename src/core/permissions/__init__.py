from rest_framework.permissions import IsAuthenticated

from src.apps.accounts.models import User


class IsOwnerOnly(IsAuthenticated):

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            if request.user.is_superuser or request.user.is_staff:
                return True
            if isinstance(obj, User):
                return obj == request.user
            return obj.user == request.user
        return False


class IsAdminOnly(IsAuthenticated):

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            if request.user.is_superuser or request.user.is_staff:
                return True
        return False
