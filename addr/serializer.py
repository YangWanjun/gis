# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import serializers

from addr import models


class PrefSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pref
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.City
        fields = '__all__'


class AzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Aza
        fields = '__all__'


class PostcodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Postcode
        fields = '__all__'
