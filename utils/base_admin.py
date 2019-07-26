from django.contrib.gis import admin


class BaseGeoAdmin(admin.OSMGeoAdmin):
    point_zoom = 16

    def has_delete_permission(self, request, obj=None):
        return False
