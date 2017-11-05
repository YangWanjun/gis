# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'pref_list', views.PrefViewSet)
router.register(r'city_list', views.CityViewSet)
router.register(r'aza_list', views.AzaViewSet)
router.register(r'postcode_list', views.PostcodeViewSet)
