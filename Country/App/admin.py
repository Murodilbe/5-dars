from django.contrib import admin
from .models import Country, CountryCompany, Building
# Register your models here.
admin.site.register(Country)
admin.site.register(CountryCompany)
admin.site.register(Building)