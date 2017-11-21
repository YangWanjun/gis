# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import googlemaps

from django.conf import settings

from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class GeocodeView(APIView):
    def get(self, request, format=None):
        address = request.GET.get('address', None)
        coordinate = {'lng': 0, 'lat': 0}
        if address:
            gmap = googlemaps.Client(key=settings.GOOGLE_MAP_KEY)
            geocode_result = gmap.geocode(address)
            if len(geocode_result) > 0 and 'geometry' in geocode_result[0]:
                geometry = geocode_result[0].get('geometry')
                address_components = geocode_result[0].get('address_components')
                countries = [item for item in address_components if item.get('short_name').upper() == "JP"]
                if len(countries) > 0:
                    coordinate = geometry.get('location')
        return Response(coordinate)
