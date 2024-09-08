from rest_framework.permissions import  BasePermission

class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        else:
            return False
class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, 'teacher') and request.user.teacher is not None
class IsStudent(BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, 'student') and request.user.student is not None