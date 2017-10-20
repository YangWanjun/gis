# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'company_list', views.CompanyViewSet)
router.register(r'line_list', views.LineViewSet)
router.register(r'station_list', views.StationViewSet)
router.register(r'station_connection_list', views.StationConnectionViewSet)
