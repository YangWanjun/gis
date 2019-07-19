from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^transform/point/$', views.SridTransformApiView.as_view(), {'category': 'point'}),
]
