from rest_framework_extensions.routers import ExtendedSimpleRouter

from . import views


router = ExtendedSimpleRouter()
router.register(r'pref', views.PrefViewSet)
router.register(r'city', views.CityViewSet)

urlpatterns = [
]

urlpatterns += router.urls
