# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'pref_list', views.PrefViewSet)
router.register(r'postcodes', views.PostcodeViewSet)
