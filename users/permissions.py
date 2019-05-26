from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):

    def has_permission(self, request, view):
        from users.api import UserAPI
        # users (GET): only admin
        # users (POST): any user
        # users/pk (GET): user authenticated or admin
        # users/pk (PUT): user authenticated or admin
        # users/pk (DELETE): user authenticated or admin
        if request.method == 'POST' or request.user.is_superuser:
            return True

        return request.user.is_authenticated and isinstance(view, UserAPI)

    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or request.user == obj
