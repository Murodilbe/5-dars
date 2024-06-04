from rest_framework import serializers
from .models import CountryCompany,Country,Building
class CountrySerializers(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class CountryCompanySerializers(serializers.ModelSerializer):
    class Meta:
        model = CountryCompany
        fields = '__all__'

class BuildingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'
