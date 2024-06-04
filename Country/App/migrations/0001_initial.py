# Generated by Django 5.0.4 on 2024-06-04 07:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Hudud nomi')),
            ],
        ),
        migrations.CreateModel(
            name='CountryCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Tashkilot nomi')),
                ('description', models.TextField(blank=True, null=True)),
                ('created', models.CharField(max_length=150, verbose_name='Tashkil topgan yili')),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='App.country')),
            ],
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Bino nomi')),
                ('country', models.CharField(max_length=150, verbose_name='Maydon kengligi')),
                ('column', models.IntegerField()),
                ('parking', models.BooleanField()),
                ('kindgarten', models.BooleanField()),
                ('elevator', models.BooleanField()),
                ('area', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='App.country')),
                ('countrycompany', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='App.countrycompany')),
            ],
        ),
    ]
