from django.db import models


class PublicManager(models.Manager):

    def __init__(self, *args, **kwargs):
        super(PublicManager, self).__init__()
        self.args = args
        self.kwargs = kwargs

    def get_queryset(self):
        return super(PublicManager, self).get_queryset().filter(is_deleted=False)


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="受付日時")
    updated_date = models.DateTimeField(auto_now=True, editable=False, verbose_name="更新日時")
    is_deleted = models.BooleanField(default=False, editable=False, verbose_name="削除フラグ")
    deleted_date = models.DateTimeField(blank=True, null=True, editable=False, verbose_name="削除年月日")

    objects = PublicManager(is_deleted=False)

    class Meta:
        abstract = True
