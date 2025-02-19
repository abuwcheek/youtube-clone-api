from rest_framework.permissions import BasePermission



class IsHasChanel(BasePermission):
    def has_permission(self, request, view):
          if request.user.is_authenticated:
               if request.user.chanel:
                    return True
          return False