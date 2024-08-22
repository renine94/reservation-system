from rest_framework.permissions import IsAuthenticated

from src.apps.accounts.models import User


class IsOwnerOnly(IsAuthenticated):

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                return True
            if isinstance(obj, User):
                return obj == request.user
            return obj.user == request.user
        return False
