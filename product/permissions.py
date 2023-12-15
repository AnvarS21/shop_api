from rest_framework.permissions import BasePermission


class IsAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner


class IsAuthotOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        return request.user == obj.owner