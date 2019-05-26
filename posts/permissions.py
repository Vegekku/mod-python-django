from django.utils import timezone
from rest_framework.permissions import BasePermission


class PostPermission(BasePermission):

    def has_permission(self, request, view):
        # posts (GET): any user
        # posts (POST): user authenticated
        # posts/pk (GET): any user
        # posts/pk (PUT): user authenticated or admin
        # posts/pk (DELETE): user authenticated or admin
        if request.user.is_superuser or request.method == 'GET':
            return True

        if request.method == 'POST' and request.user.is_authenticated:
            return True

        from posts.api import PostAPI
        return request.user.is_authenticated and isinstance(view, PostAPI)

    def has_object_permission(self, request, view, obj):

        if request.method == 'GET':
            return request.user.is_superuser or obj.author == request.user or obj.publish_date <= timezone.now()

        return request.user.is_superuser or obj.author == request.user
