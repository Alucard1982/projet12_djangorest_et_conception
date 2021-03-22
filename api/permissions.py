from rest_framework import permissions

from api.models import User, Role, Client


class IsGestionnaire(permissions.BasePermission):

    def has_permission(self, request, view):
        # Instance must have an attribute named `owner`.

        users_gestion = User.objects.filter(role__type="gestion")
        if request.user in users_gestion:
            return users_gestion


class IsSupportGestionEvent(permissions.BasePermission):

    def has_permission(self, request, view):
        # Instance must have an attribute named `owner`.

        users_support = User.objects.filter(role__type="support")
        users_gestion = User.objects.filter(role__type="gestion")
        if request.user in users_support:
            return users_support
        elif request.user in users_gestion:
            return users_gestion


class IsSalerGestionClient(permissions.BasePermission):

    def has_permission(self, request, view):
        # Instance must have an attribute named `owner`.
        users_salers = User.objects.filter(role__type="vente")
        users_gestion = User.objects.filter(role__type="gestion")
        if request.user in users_salers:
            return users_salers
        elif request.user in users_gestion:
            return users_gestion
