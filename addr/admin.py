# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from . import models


# Register your models here.
@admin.register(models.Pref)
class PrefAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')


@admin.register(models.Postcode)
class PostcodeAdmin(admin.ModelAdmin):
    pass
