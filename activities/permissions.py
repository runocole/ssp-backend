from rest_framework.permissions import BasePermission

class IsActivityOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user