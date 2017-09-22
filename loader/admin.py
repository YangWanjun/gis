# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.gis import admin

from loader.models import AzaCode


class AzaCodeAdmin(admin.OSMGeoAdmin):
    list_display = ['city_code', 'jusho1', 'jusho2', 'jusho3', 'jcode1', 'jcode2', 'lon', 'lat']
    search_fields = ['city_code', 'jusho1', 'jusho2', 'jusho3']

# Register your models here.
admin.site.register(AzaCode, AzaCodeAdmin)
