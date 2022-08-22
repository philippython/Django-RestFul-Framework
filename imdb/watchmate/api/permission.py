from rest_framework.permissions import BasePermission, IsAdminUser

class AdminOnly(BasePermission):

    def has_permisssions(self, request, view):
        return bool(request.user and request.user.is_staff)
