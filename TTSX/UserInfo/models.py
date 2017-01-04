#encoding:utf-8
from django.db import models

# Create your models here.
class UserInfo(models.Model):
    """用户信息"""
    uName = models.CharField(max_length=20, db_column='uname', unique=True)
    uPwd = models.CharField(max_length=20, db_column='upwd')
    uEmail = models.CharField(max_length=30, db_column='uemail')
    isDeleted = models.BooleanField(default=False)

    class Meta():
        """通过元类定义表名"""
        db_table = "UserInfo"



class DeliveryAddress(models.Model):
    """收货信息"""
    daOwner = models.ForeignKey(UserInfo, db_column='owner', null=True)
    daName = models.CharField(max_length=20, db_column='name')
    daPhone = models.CharField(max_length=11, db_column='phone')
    daAddress = models.CharField(max_length=50, db_column='address')
    daPostCode = models.CharField(max_length=6, db_column='postcode')
    class Meta():
        """通过元类定义表名"""
        db_table = "DeliveryAddress"
