from rest_framework import permissions
from rest_framework.decorators import permission_classes


class IsOwner(permissions.BasePermission):
    """Проверяет, является ли пользователь владельцем."""

    def has_object_permission(self, request, view, obj):
        if obj.author == request.user:
            return True
        return False


class IsModer(permissions.BasePermission):
    """Проверяет, является ли пользователь модератором."""

    message = "Вы не являетесь модератором"

    def has_permission(self, request, view):
        return request.user.groups.filter(name="moder").exists()
