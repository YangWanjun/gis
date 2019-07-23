from . import models, serializers
from utils.base_rest import BaseReadOnlyGeoModelViewSet


class PrefViewSet(BaseReadOnlyGeoModelViewSet):
    queryset = models.Pref.objects.all()
    serializer_class = serializers.PrefSerializer
    search_fields = ('pref_code', 'pref_name')


class CityViewSet(BaseReadOnlyGeoModelViewSet):
    queryset = models.City.objects.all()
    serializer_class = serializers.CitySerializer
    search_fields = ('city_code', 'city_name')
