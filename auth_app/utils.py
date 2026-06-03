from rest_framework.permissions import BasePermission

class GroupPermission(BasePermission):
    group_name = None

    def has_permission(self, request, view):
        user = request.user

        if not user or not user.is_authenticated:
            return False

        if user.is_superuser:
            return True

        return user.groups.filter(name=self.group_name).exists()

class EstudiosPermission(GroupPermission):
    group_name = "estudios"

class ComunicacionPermission(GroupPermission):
    group_name = "comunicacion"