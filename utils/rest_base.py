from rest_framework import status as rest_status
from rest_framework.views import APIView, exception_handler
from rest_framework.response import Response

from . import constants
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
