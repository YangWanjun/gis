from . import models, serializers
from utils.base_rest import BaseReadOnlyModelLayerViewSet, BaseModelLayerViewSet


# Create your views here.
class CompanyViewSet(BaseReadOnlyModelLayerViewSet):
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer
    search_fields = ('company_code', 'company_name')


class RouteViewSet(BaseReadOnlyModelLayerViewSet):
    queryset = models.Route.objects.all()
    serializer_class = serializers.RouteSerializer
    search_fields = ('line_code', 'line_name')


class StationViewSet(BaseReadOnlyModelLayerViewSet):
    queryset = models.Station.objects.all()
    serializer_class = serializers.StationSerializer
    geo_serializer_class = serializers.StationLayerSerializer
    search_fields = ('line_code', 'line_name')


class JoinStationViewSet(BaseModelLayerViewSet):
    queryset = models.JoinStation.objects.all()
    serializer_class = serializers.JoinStationSerializer
