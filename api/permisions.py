from rest_framework.permissions import BasePermission


class UserAPIPermission(BasePermission):


    def has_object_permission(self, request, view, obj):
        return obj == request.user


class UserListAPIPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff:
            return request.user.is_staff


