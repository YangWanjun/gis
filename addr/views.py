# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import  viewsets, filters

from addr import models
from addr import serializer


# Create your views here.
class PrefViewSet(viewsets.ModelViewSet):
    queryset = models.Pref.objects.public_all()
    serializer_class = serializer.PrefSerializer
    filter_fields = ('code', 'name')


class CityViewSet(viewsets.ModelViewSet):
    queryset = models.City.objects.public_all()
    serializer_class = serializer.CitySerializer
    filter_fields = ('code', 'name')


class AzaViewSet(viewsets.ModelViewSet):
    queryset = models.Aza.objects.public_all()
    serializer_class = serializer.AzaSerializer
    filter_fields = ('code', 'name')


class PostcodeViewSet(viewsets.ModelViewSet):
    queryset = models.Postcode.objects.public_all()
    serializer_class = serializer.PostcodeSerializer
    filter_fields = ('post_code',)
