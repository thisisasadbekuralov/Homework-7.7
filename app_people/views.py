from rest_framework import viewsets, permissions

from app_qatagon.models import AffectedIndividual
from app_qatagon.serializers import AffectedIndividualDetailSerializer


class AffectedIndividualsPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        elif request.method == "POST":
            return request.user.is_authenticated
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        return obj.user == request.user


class AffectedIndividualsViewSet(viewsets.ModelViewSet):
    queryset = AffectedIndividual.objects.all()
    serializer_class = AffectedIndividualDetailSerializer
    permission_classes = [AffectedIndividualsPermission]