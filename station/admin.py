from django.contrib.gis import admin

from . import models
from utils.base_admin import BaseGeoAdmin


# Register your models here.
@admin.register(models.Company)
class CompanyAdmin(BaseGeoAdmin):
    list_display = ('company_code', 'company_name', 'company_type', 'status')
    list_display_links = ('company_code', 'company_name')
    list_filter = ('company_type', 'status')
    search_fields = ('company_name',)


@admin.register(models.Route)
class RouteAdmin(BaseGeoAdmin):
    list_display = ('line_code', 'line_name', 'company', 'line_type', 'status')
    list_display_links = ('line_code', 'line_name')
    list_filter = ('line_type', 'status')
    search_fields = ('line_name',)


@admin.register(models.Station)
class StationAdmin(BaseGeoAdmin):
    list_display = ('station_code', 'station_name', 'route', 'address', 'status')
    list_display_links = ('station_code', 'station_name')
    list_filter = ('status',)
    search_fields = ('station_name', 'address')

