from rest_framework import serializers

from . import models
from utils.base_rest import BaseGeoFeatureModelSerializer, BaseModelSerializer


class PrefSerializer(BaseModelSerializer):

    class Meta:
        model = models.Pref
        exclude = ('mpoly',)


class PrefLayerSerializer(BaseGeoFeatureModelSerializer):

    class Meta:
        model = models.Pref
        geo_field = 'mpoly'
        fields = '__all__'


class CitySerializer(BaseModelSerializer):

    class Meta:
        model = models.City
        exclude = ('mpoly',)


class CityLayerSerializer(BaseGeoFeatureModelSerializer):

    class Meta:
        model = models.City
        geo_field = 'mpoly'
        fields = '__all__'


class TownSerializer(BaseModelSerializer):

    class Meta:
        model = models.Town
        exclude = ('mpoly',)


class TownLayerSerializer(BaseGeoFeatureModelSerializer):

    class Meta:
        model = models.Town
        geo_field = 'mpoly'
        fields = '__all__'


class PostcodeSerializer(BaseModelSerializer):
    address = serializers.CharField(read_only=True, label='住所')

    class Meta:
        model = models.Postcode
        fields = '__all__'
