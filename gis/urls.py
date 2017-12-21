"""gis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers

from addr import views as address_views
from station import views as station_views
from geocode import views as geocode_views


router = routers.DefaultRouter()
router.register(r'pref_list', address_views.PrefViewSet)
router.register(r'city_list', address_views.CityViewSet)
router.register(r'aza_list', address_views.AzaViewSet)
router.register(r'postcode_list', address_views.PostcodeViewSet)

router.register(r'company_list', station_views.CompanyViewSet)
router.register(r'line_list', station_views.LineViewSet)
router.register(r'station_list', station_views.StationViewSet)
router.register(r'station_connection_list', station_views.StationConnectionViewSet)

router.register(r'geocode', geocode_views.GeocodeViewSet, base_name='geocode')

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^api/', include(router.urls)),
]
