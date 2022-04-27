from rest_framework import permissions


class IsCommunityManager(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return request.user.is_authenticated and user.duties == 'community manager'

class IsCEO(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return request.user.is_authenticated and user.duties == 'CEO'

class IsITSupport(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return request.user.is_authenticated and user.duties == 'IT Support'

class IsAccountant(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return request.user.is_authenticated and user.duties == 'Accountant'