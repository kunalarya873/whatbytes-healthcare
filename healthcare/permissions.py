from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsPatiendOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        # __define-ocg__: Only allow access to objects created by the user
        return obj.created_by == request.user
