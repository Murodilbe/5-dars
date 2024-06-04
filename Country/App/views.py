from django.shortcuts import render
from .serializers import CountrySerializers, CountryCompanySerializers, BuildingSerializers
# Create your views here.
from rest_framework import permissions
from .models import Country,CountryCompany,Building
from rest_framework import viewsets
from rest_framework.response import Response
class CountryViewSet(viewsets.ModelViewSet):
    serializer_class = CountrySerializers
    permission_classes = [permissions.DjangoModelPermissions]

    def get_queryset(self):
        return Country.objects.all()
class BuildingsViewSet(viewsets.ModelViewSet):
    serializer_class = BuildingSerializers
    permission_classes = [permissions.DjangoModelPermissions]

    def get_queryset(self):
        return Building.objects.all()

class CountryCompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CountryCompanySerializers
    permission_classes = [permissions.DjangoModelPermissions]


    def get_queryset(self):
        return CountryCompany.objects.all()
