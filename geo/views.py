from . import biz
from utils import constants, common
from utils.errors import CustomException
from utils.base_rest import BaseApiView


# Create your views here.
class SridTransformApiView(BaseApiView):
    """座標を変換する

    lng: 経度
    lat: 緯度
    srid_from: 変更前の測地系
    srid_to: 変更後の測地系
    """

    def get_context_data(self, **kwargs):
        category = kwargs.get('category')
        srid_from = self.request.data.get('srid_from', None) or self.request.GET.get('srid_from', None)
        srid_to = self.request.data.get('srid_to', None) or self.request.GET.get('srid_to', None)
        if not srid_from:
            raise CustomException(constants.ERROR_FIELD_REQUIRED.format(name='変更前のSRID'))
        elif not srid_to:
            raise CustomException(constants.ERROR_FIELD_REQUIRED.format(name='変更後のSRID'))
        elif not common.is_digit(srid_from) or not common.is_digit(srid_to):
            raise CustomException(constants.ERROR_REQUIRED_DIGIT.format(name='SRID'))
        if category == constants.SRID_TRANSFORM_CATEGORY_POINT:
            lng = self.request.data.get('lng', None) or self.request.GET.get('lng', None)
            lat = self.request.data.get('lat', None) or self.request.GET.get('lat', None)
            lng, lat = biz.transform_point(lng, lat, srid_from=srid_from, srid_to=srid_to)
            return {'lng': lng, 'lat': lat}
        else:
            return {}
