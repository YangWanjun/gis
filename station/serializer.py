# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import serializers

from . import models


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = '__all__'


class LineSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Line
        fields = '__all__'


class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Station
        fields = '__all__'


class StationConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StationConnection
        fields = '__all__'
