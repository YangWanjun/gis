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


class ChomeSerializer(BaseModelSerializer):

    class Meta:
        model = models.Chome
        exclude = ('mpoly',)


class ChomeLayerSerializer(BaseGeoFeatureModelSerializer):

    class Meta:
        model = models.Chome
        geo_field = 'mpoly'
        fields = '__all__'


class PostcodeSerializer(BaseModelSerializer):

    class Meta:
        model = models.Postcode
        fields = '__all__'
