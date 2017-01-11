#encoding:utf-8
from django.db import models
from UserInfo.models import UserInfo
from GoodsInfo.models import GoodsInfo

# Create your models here.
class OrderInfo(models.Model):
    """订单信息"""
    oUser = models.ForeignKey(UserInfo, db_column='user')
    oTotal = models.DecimalField(max_digits=10, decimal_places=2, db_column='ototal')
    oTime = models.DateTimeField(auto_now_add=True, db_column='otime')
    oState = models.BooleanField(default=False, db_column='state')
    class Meta():
        """通过元类定义表名"""
        db_table = "OrderInfo"
        ordering = ['-id']

    def __unicode__(self):
        """打印对象返回订单用户的名字"""
        return self.oUser.uName

class OrderDetailInfo(models.Model):
    """订单详细信息"""
    oiOrder = models.ForeignKey(OrderInfo, db_column='order')
    oiGoods = models.ForeignKey(GoodsInfo, db_column="goods")
    oiCount = models.IntegerField(db_column='count')
    oiPrice = models.DecimalField(max_digits=10, decimal_places=2, db_column='price')
    class Meta():
        """通过元类定义表名"""
        db_table = "OrderDetailInfo"