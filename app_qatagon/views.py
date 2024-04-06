from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from .models import Event, AffectedIndividual

from .serializers import AffectedIndividualSerializer, AffectedIndividualDetailSerializer, \
    AffectedIndividualsCreateSerializer, AffectedIndividualUpdateAPIView, AffectedIndividualDeleteAPIView


class AffectedIndividualAPIView(ListAPIView): # Get
    queryset = AffectedIndividual.objects.all()
    serializer_class = AffectedIndividualSerializer


class AffectedIndividualDetailView(RetrieveAPIView): #Get
    queryset = AffectedIndividual.objects.all()
    serializer_class = AffectedIndividualDetailSerializer


class AffectedIndividualsCreateView(CreateAPIView): #Post
    queryset = AffectedIndividual.objects.all()
    serializer_class = AffectedIndividualsCreateSerializer


class AffectedIndividualsUpdateView(UpdateAPIView): #Patch, Put
    queryset = AffectedIndividual.objects.all()
    serializer_class = AffectedIndividualUpdateAPIView


class AffectedIndividualsDeleteView(DestroyAPIView): #Delete
    queryset = AffectedIndividual.objects.all()
    serializer_class = AffectedIndividualDeleteAPIView