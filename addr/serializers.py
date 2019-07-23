from . import models
from utils.base_rest import BaseGeoFeatureModelSerializer


class PrefSerializer(BaseGeoFeatureModelSerializer):

    class Meta:
        model = models.Pref
        geo_field = 'mpoly'
        fields = '__all__'


class CitySerializer(BaseGeoFeatureModelSerializer):

    class Meta:
        model = models.City
        geo_field = 'mpoly'
        fields = '__all__'
