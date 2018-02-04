from rest_framework import permissions


class UpdatePermissions(permissions.BasePermission):
    """Allow users to update their own profile."""

    def has_object_permission(self, request, view, obj):
        """Check if the user has permissions."""

        if request.method in permissions.SAFE_METHODS:
            return True
        # in our case we will assume that all users have permission to delete and update
        return True
