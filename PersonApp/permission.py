from rest_framework.permissions import BasePermission

class HasAccessToPersonCheckList(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.groups.filter(name='person_checklist_users').exists()
