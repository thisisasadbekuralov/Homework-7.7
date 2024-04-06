from rest_framework import serializers
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from .models import Event, AffectedIndividual


class AffectedIndividualSerializer(serializers.ModelSerializer): #Get
    people = serializers.SerializerMethodField(read_only=True, source='get_people')


    class Meta:
        model = AffectedIndividual
        fields = ['id', 'name', 'person_image', 'people']


    def get_people(self, obj):
        return f'http://127.0.0.1:8000/qaragon/{obj.id}'


class AffectedIndividualDetailSerializer(serializers.ModelSerializer): #Get
    class Meta:
        model = AffectedIndividual
        fields = "__all__"


class AffectedIndividualsCreateSerializer(serializers.ModelSerializer): #Post
    class Meta:
        model = AffectedIndividual
        fields = "__all__"


class AffectedIndividualUpdateAPIView(UpdateAPIView): #Patch, Put
    queryset = AffectedIndividual.objects.all()
    serializer_class = AffectedIndividualSerializer


class AffectedIndividualDeleteAPIView(DestroyAPIView): #Delete
    queryset = AffectedIndividual.objects.all()
    serializer_class = AffectedIndividualSerializer