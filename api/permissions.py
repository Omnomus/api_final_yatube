from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, post):
        return (request.method in permissions.SAFE_METHODS
                or request.user == post.author)
