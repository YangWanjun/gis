from . import models, serializers
from utils.base_rest import BaseReadOnlyModelViewSet


class PrefViewSet(BaseReadOnlyModelViewSet):
    queryset = models.Pref.objects.all()
    serializer_class = serializers.PrefSerializer
    geo_serializer_class = serializers.PrefLayerSerializer
    search_fields = ('pref_code', 'pref_name')


class CityViewSet(BaseReadOnlyModelViewSet):
    queryset = models.City.objects.all()
    serializer_class = serializers.CitySerializer
    geo_serializer_class = serializers.CityLayerSerializer
    search_fields = ('city_code', 'city_name')
