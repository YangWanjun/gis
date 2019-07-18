from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^srid-transform/(?P<category>point|point-array)/$', views.SridTransformApiView.as_view(),),
]
