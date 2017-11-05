# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.gis import admin

from . import models
from utils.django_base import BaseAdmin


# Register your models here.
@admin.register(models.Pref)
class PrefAdmin(BaseAdmin):
    list_display = ('code', 'name')


@admin.register(models.City)
class CityAdmin(BaseAdmin):
    list_display = ('pref', 'code', 'name')
    list_display_links = ('code',)
    search_fields = ('pref__name', 'code', 'name')


@admin.register(models.Aza)
class AzaAdmin(BaseAdmin):
    list_display = ('pref', 'city', 'code', 'name')
    list_display_links = ('code',)
    search_fields = ('pref__name', 'city__name', 'code', 'name')


@admin.register(models.Postcode)
class PostcodeAdmin(admin.ModelAdmin):
    list_display = ('city_code', 'post_code', 'pref_name', 'city_name', 'town_name')
    list_display_links = ('post_code',)
    search_fields = ('city_code', 'post_code', 'pref_name', 'city_name', 'town_name')
