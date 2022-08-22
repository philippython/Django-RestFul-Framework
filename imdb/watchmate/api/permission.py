from rest_framework.permissions import BasePermission, IsAdminUser

class AdminOrReadOnly(IsAdminUser):

    def has_permisssions(self, request, view):
        admin_permission = bool(request.user and request.user.is_staff)
        return request.methodd == 'GET'or admin_permission