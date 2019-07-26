from . import models
from utils.base_rest import BaseGeoFeatureModelSerializer, BaseModelSerializer


class CompanySerializer(BaseModelSerializer):

    class Meta:
        model = models.Company
        fields = '__all__'


class RouteSerializer(BaseModelSerializer):

    class Meta:
        model = models.Route
        fields = '__all__'


class StationSerializer(BaseModelSerializer):

    class Meta:
        model = models.Station
        exclude = ('point',)


class StationLayerSerializer(BaseGeoFeatureModelSerializer):

    class Meta:
        model = models.Station
        geo_field = 'point'
        fields = '__all__'


class JoinStationSerializer(BaseModelSerializer):

    class Meta:
        model = models.JoinStation
        fields = '__all__'
