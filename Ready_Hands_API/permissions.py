from rest_framework.permissions import BasePermission
from rolepermissions.checkers import has_permission


class IsClient(BasePermission):
    def has_permission(self, request, view,):
        return has_permission(request.user, 'is_client')


class IsWorker(BasePermission):
    def has_permission(self, request, view,):
        return has_permission(request.user, 'is_worker')
