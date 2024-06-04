from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=150, verbose_name='Hudud nomi')


    def __str__(self):
        return self.name


class CountryCompany(models.Model):
    name = models.CharField(max_length=150,verbose_name='Tashkilot nomi')
    description = models.TextField(blank=True,null=True)
    created = models.CharField(max_length=150, verbose_name='Tashkil topgan yili')
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)



    def __str__(self):
        return self.name


class Building(models.Model):
    name = models.CharField(max_length=150, verbose_name='Bino nomi')
    countrycompany = models.ForeignKey(CountryCompany,on_delete=models.SET_NULL,null=True, verbose_name='Tashkilot nomi')
    area = models.ForeignKey(Country,on_delete=models.SET_NULL, null=True, verbose_name='Maydon kengligi')
    country = models.CharField(max_length=150, verbose_name='Maydon kengligi')
    column = models.IntegerField(verbose_name='Necha qavatdan iborat')
    parking = models.BooleanField(verbose_name='Avtoturargoh')
    kindgarten = models.BooleanField(verbose_name='Bolalar maydonchasi')
    elevator = models.BooleanField(verbose_name='Lift')


    def __str__(self):
        return self.name
