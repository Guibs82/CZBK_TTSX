#encoding:utf-8
from django.db import models
from UserInfo.models import UserInfo
from GoodsInfo.models import GoodsInfo

# Create your models here.
class CartInfo(models.Model):
    """购物车信息"""
    cUser = models.ForeignKey('UserInfo', db_column='user')
    cGoods = models.ForeignKey('GoodsInfo', db_column='goods')
    cCount = models.IntegerField(db_column='count')
    class Meta():
        """通过元类定义表名"""
        db_table = "CartInfo"