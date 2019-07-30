from django.contrib.gis import admin

from . import models
from utils.base_admin import BaseGeoAdmin


# Register your models here.
@admin.register(models.Pref)
class PrefAdmin(BaseGeoAdmin):
    list_display = ('pref_code', 'pref_name', 'people_count', 'family_count')
    list_display_links = ('pref_code', 'pref_name')
    search_fields = ('pref_code', 'pref_name')


@admin.register(models.City)
class CityAdmin(BaseGeoAdmin):
    list_display = ('pref_name', 'city_code', 'city_name', 'people_count', 'family_count')
    list_display_links = ('city_code', 'city_name')
    search_fields = ('city_code', 'city_name')
    list_filter = ('pref_name',)


@admin.register(models.Chome)
class ChomeAdmin(BaseGeoAdmin):
    list_display = ('pref_name', 'city_name', 'chome_code', 'chome_name')
    list_display_links = ('chome_code', 'chome_name')
    search_fields = ('chome_code', 'chome_name')
