from django.contrib.gis import admin


class BaseGeoAdmin(admin.OSMGeoAdmin):

    def has_delete_permission(self, request, obj=None):
        return False
