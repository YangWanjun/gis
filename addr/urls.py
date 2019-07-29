from rest_framework_extensions.routers import ExtendedSimpleRouter

from . import views


router = ExtendedSimpleRouter()
pref_router = router.register(r'pref', views.PrefViewSet)
pref_router.register(
    r'city',
    views.CityViewSet,
    basename='pref-city',
    parents_query_lookups=['pref_code'],
)
city_router = router.register(r'city', views.CityViewSet)
city_router.register(
    r'chome',
    views.ChomeViewSet,
    basename='pref-city-chome',
    parents_query_lookups=['city_code'],
)
router.register(r'chome', views.ChomeViewSet)

urlpatterns = [
]

urlpatterns += router.urls
