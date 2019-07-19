from django.contrib.gis import admin

from . import models
from utils.base_admin import BaseGeoAdmin


# Register your models here.
@admin.register(models.City)
class CityAdmin(BaseGeoAdmin):
    list_display = ('pref_code', 'pref_name', 'city_code', 'city_name')
    list_display_links = ('city_code', 'city_name')
    search_fields = ('city_code', 'city_name')


@admin.register(models.Chome)
class ChomeAdmin(BaseGeoAdmin):
    list_display = ('pref_name', 'city_name', 'chome_code', 'chome_name')
    list_display_links = ('chome_code', 'chome_name')
    search_fields = ('chome_code', 'chome_name')
