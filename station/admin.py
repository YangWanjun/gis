# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.gis import admin
from . import models
from utils.django_base import BaseAdmin


# Register your models here.
@admin.register(models.Company)
class CompanyAdmin(BaseAdmin):
    list_display = ('code', 'name')
    search_fields = ('code', 'name')


@admin.register(models.Line)
class LineAdmin(BaseAdmin):
    list_display = ('code', 'name')
    search_fields = ('code', 'name')


@admin.register(models.Station)
class StationAdmin(BaseAdmin):
    default_zoom = 18
    list_display = ('code', 'name', 'line', 'pref', 'post_code', 'address')
    search_fields = ('code', 'name')


@admin.register(models.StationConnection)
class StationConnectionAdmin(BaseAdmin):
    list_display = ('line', 'station1', 'station2')
    search_fields = ('line__name', 'station1__name', 'station2__name')
