# permissions.py
from rest_framework import permissions
from django.utils import timezone


class IsTaskOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsTaskOwnerAndNotPastDeadline(permissions.BasePermission):
    """
    Custom permission to only allow the owner of a task to view or edit it if the deadline has not passed.
    """

    def has_object_permission(self, request, view, obj):
        # Check if the user is the owner of the task
        if obj.owner == request.user:
            # Check if the deadline has not passed
            if obj.deadline is None or obj.deadline > timezone.now():
                return True
        return False
