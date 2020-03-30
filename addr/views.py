from rest_framework_extensions.mixins import NestedViewSetMixin
from rest_framework.response import Response

from . import models, serializers
from utils.base_rest import BaseReadOnlyModelLayerViewSet, BaseReadOnlyModelViewSet


class PrefViewSet(NestedViewSetMixin, BaseReadOnlyModelLayerViewSet):
    queryset = models.Pref.objects.all()
    serializer_class = serializers.PrefSerializer
    geo_serializer_class = serializers.PrefLayerSerializer
    search_fields = ('pref_code', 'pref_name')

    def retrieve(self, request, *args, **kwargs):
        return super(PrefViewSet, self).retrieve(request, *args, **kwargs)


class CityViewSet(NestedViewSetMixin, BaseReadOnlyModelLayerViewSet):
    queryset = models.City.objects.all()
    serializer_class = serializers.CitySerializer
    geo_serializer_class = serializers.CityLayerSerializer
    search_fields = ('pref__pref_code', 'pref_name', 'city_code', 'city_name')

    def list(self, request, *args, **kwargs):
        return super(CityViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(CityViewSet, self).retrieve(request, *args, **kwargs)


class ChomeViewSet(NestedViewSetMixin, BaseReadOnlyModelLayerViewSet):
    queryset = models.Chome.objects.all()
    serializer_class = serializers.ChomeSerializer
    geo_serializer_class = serializers.ChomeLayerSerializer
    search_fields = ('pref__pref_code', 'pref_name', 'city__city_code', 'city_name', 'chome_code', 'chome_name')

    def list(self, request, *args, **kwargs):
        return super(ChomeViewSet, self).list(request, *args, **kwargs)


class PostcodeViewSet(BaseReadOnlyModelViewSet):
    """/api/addr/postcode/?code={}で検索してください。
    """
    pagination_class = None
    queryset = models.Postcode.objects.all()
    serializer_class = serializers.PostcodeSerializer

    def get_queryset(self):
        qs = super(PostcodeViewSet, self).get_queryset()
        if 'code' in self.request.GET:
            return qs.filter(post_code=self.request.GET.get('code'))
        else:
            return qs.none()
