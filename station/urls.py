from rest_framework_extensions.routers import ExtendedSimpleRouter

from . import views


router = ExtendedSimpleRouter()
router.register(r'company', views.CompanyViewSet)
router.register(r'route', views.RouteViewSet)
router.register(r'station', views.StationViewSet)
router.register(r'join-station', views.JoinStationViewSet)

urlpatterns = [
]

urlpatterns += router.urls

