from warnings import filters as warn_filters

from rest_framework import viewsets, permissions
from django_filters import rest_framework as django_filters
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView
)
from rest_framework.permissions import IsAuthenticated

from .models import Event, AffectedIndividual
from .serializers import (
    AffectedIndividualSerializer,
    AffectedIndividualDetailSerializer,
    AffectedIndividualsCreateSerializer
)


class AffectedIndividualFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = AffectedIndividual
        fields = ['name']


class AffectedIndividualAPIView(ListAPIView):  # Get
    queryset = AffectedIndividual.objects.all()
    serializer_class = AffectedIndividualSerializer
    filter_backends = [django_filters.DjangoFilterBackend]
    filterset_class = AffectedIndividualFilter


class AffectedIndividualDetailView(RetrieveAPIView):  # Get
    queryset = AffectedIndividual.objects.all()
    serializer_class = AffectedIndividualDetailSerializer


class AffectedIndividualsCreateView(CreateAPIView):  # Post
    queryset = AffectedIndividual.objects.all()
    serializer_class = AffectedIndividualsCreateSerializer
    permission_classes = [IsAuthenticated]


class AffectedIndividualsUpdateView(RetrieveUpdateAPIView):  # Patch, Put
    queryset = AffectedIndividual.objects.all()
    serializer_class = AffectedIndividualDetailSerializer
    http_method_names = ["patch", "put"]
    permission_classes = [IsAuthenticated]



class AffectedIndividualsDeleteView(DestroyAPIView):  # Delete
    queryset = AffectedIndividual.objects.all()
    serializer_class = AffectedIndividualDetailSerializer
    permission_classes = [IsAuthenticated]

