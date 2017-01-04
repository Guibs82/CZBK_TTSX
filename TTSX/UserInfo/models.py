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