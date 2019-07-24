import json

from django.contrib.gis.geos.geometry import GEOSGeometry

from rest_framework import status as rest_status, serializers, viewsets
from django.contrib.gis.geos import Polygon
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework.response import Response
from rest_framework.views import APIView, exception_handler

from . import constants, common
from .errors import CustomException


class BaseApiView(APIView):

    def get_context_data(self, **kwargs):
        pass

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return Response(context)

    def post(self, request, *args, **kwargs):
        pass


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['status_code'] = response.status_code
    elif isinstance(exc, CustomException):
        response = Response({'detail': exc.message}, status=rest_status.HTTP_400_BAD_REQUEST)

    return response


class GeoSearchMixin(object):
    geo_serializer_class = None

    def check_boundary(self, request):
        """レイヤー表示時、パフォーマンスを上がるため、ズームレベルと境界が必要です。

        :param request:
        :return: ズームレベルと境界のTupleを返す
        """
        if request.data:
            zoom = request.data.get('zoom', None)
            boundary = request.data.get('boundary', None)
        else:
            params = common.parse_querystring(request.query_params)
            zoom = params.get('zoom', None)
            boundary = params.get('boundary', None)
        if not zoom \
                or not boundary \
                or 'left' not in boundary \
                or 'bottom' not in boundary \
                or 'right' not in boundary \
                or 'top' not in boundary:
            raise CustomException(constants.ERROR_INVALID_LAYER_SEARCH)
        else:
            zoom = int(zoom)
            for key, value in boundary.items():
                boundary[key] = float(value)
            return zoom, boundary

    @action(methods=['GET'], url_path='layer', detail=False)
    def layer(self, request, *args, **kwargs):
        """レイヤー表示

        :param request:
        :param args:
        :param kwargs:
        :return: GeoJSONを返す
        """
        zoom, boundary = self.check_boundary(request, *args, **kwargs)
        mpoly = Polygon((
            (boundary.get('left'), boundary.get('bottom')),
            (boundary.get('right'), boundary.get('bottom')),
            (boundary.get('right'), boundary.get('top')),
            (boundary.get('left'), boundary.get('top')),
            (boundary.get('left'), boundary.get('bottom')),
        ),)
        queryset = self.filter_queryset(self.get_queryset()).filter(mpoly__intersects=mpoly)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_geo_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_geo_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_geo_serializer(self, *args, **kwargs):
        serializer_class = self.get_geo_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)

    def get_geo_serializer_class(self):
        assert self.geo_serializer_class is not None, (
            "'%s' should either include a `serializer_class` attribute, "
            "or override the `get_serializer_class()` method."
            % self.__class__.__name__
        )

        return self.geo_serializer_class


class BaseReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet, GeoSearchMixin):

    filter_backends = [SearchFilter]


class BaseModelSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        data = super(BaseModelSerializer, self).to_representation(instance)
        for name in ('created_date', 'updated_date', 'is_deleted', 'deleted_date'):
            if name in data:
                del data[name]
        return data


class BaseGeoFeatureModelSerializer(GeoFeatureModelSerializer):

    def to_representation(self, instance):
        feature = super(BaseGeoFeatureModelSerializer, self).to_representation(instance)
        field = self.fields[self.Meta.geo_field]
        value = field.model_field.value_from_object(instance)
        if isinstance(value, GEOSGeometry):
            feature["geometry"] = json.loads(value.geojson)
        return feature
