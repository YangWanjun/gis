import json

from django.contrib.gis.geos.geometry import GEOSGeometry

from rest_framework import status as rest_status, serializers, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView, exception_handler
from rest_framework.response import Response
from rest_framework_gis.serializers import GeoFeatureModelSerializer

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

    def check_boundary(self, request, *args, **kwargs):
        request = self.initialize_request(request, *args, **kwargs)
        if request.data:
            zoom = request.data.get('zoom', None)
            boundary = request.data.get('boundary', None)
        else:
            params = common.parse_querystring(request.query_params)
            zoom = params.get('zoom', None)
            boundary = params.get('boundary', None)
        if not zoom or not boundary:
            self.headers = self.default_response_headers  # deprecate?
            raise CustomException(constants.ERROR_INVALID_LAYER_SEARCH)
        else:
            return True


class BaseModelSerializer(serializers.ModelSerializer):
    pass


class BaseReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):

    filter_backends = [SearchFilter]


class BaseReadOnlyGeoModelViewSet(BaseReadOnlyModelViewSet, GeoSearchMixin):

    def dispatch(self, request, *args, **kwargs):
        try:
            self.check_boundary(request, *args, **kwargs)
            return super(BaseReadOnlyModelViewSet, self).dispatch(request, *args, **kwargs)
        except Exception as ex:
            response = self.handle_exception(ex)
            return self.finalize_response(request, response, *args, **kwargs)


class BaseGeoFeatureModelSerializer(GeoFeatureModelSerializer):

    def to_representation(self, instance):
        feature = super(BaseGeoFeatureModelSerializer, self).to_representation(instance)
        field = self.fields[self.Meta.geo_field]
        value = field.model_field.value_from_object(instance)
        if isinstance(value, GEOSGeometry):
            feature["geometry"] = json.loads(value.geojson)
        return feature
