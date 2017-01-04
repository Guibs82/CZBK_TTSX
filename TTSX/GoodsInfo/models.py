#encoding:utf-8
from django.db import models

# Create your models here.
class TypeInfo(models.Model):
    """商品分类"""
    tTitle = models.CharField(max_length=20, db_column='ttitle')
    isDeleted = models.BooleanField(default=False)
    class Meta():
        """通过元类定义表名"""
        db_table = "TypeInfo"

class GoodsInfo(models.Model):
    """商品信息"""
    gTitle = models.CharField(max_length=20, db_column='gtitle')
    gType = models.ForeignKey(TypeInfo, db_column='gtype')
    gImage = models.CharField(max_length=100, db_column='gimage')
    gPrice = models.DecimalField(max_digits=10, decimal_places=2, db_column='gprice')
    gDesc = models.TextField(max_length=500, db_column='gdesc')
    isDeleted = models.BooleanField(default=False)
    class Meta():
        """通过元类定义表名"""
        db_table = "GoodsInfo"