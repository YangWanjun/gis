# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets, filters

from . import models
from . import serializer


# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = models.Company.objects.public_all()
    serializer_class = serializer.CompanySerializer
    filter_fields = ('code', 'name')


class LineViewSet(viewsets.ModelViewSet):
    queryset = models.Line.objects.public_all()
    serializer_class = serializer.LineSerializer
    filter_fields = ('code', 'name')


class StationViewSet(viewsets.ModelViewSet):
    queryset = models.Station.objects.public_all()
    serializer_class = serializer.StationSerializer
    filter_fields = ('code', 'name')


class StationConnectionViewSet(viewsets.ModelViewSet):
    queryset = models.StationConnection.objects.public_all()
    serializer_class = serializer.StationConnectionSerializer
    filter_fields = ('line', 'station1', 'station2')
