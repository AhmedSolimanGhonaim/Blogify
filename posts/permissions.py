from typing import override
from rest_framework.permissions import BasePermission

class IsAuthorOrReadOnly(BasePermission):


    
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.auth == request.user