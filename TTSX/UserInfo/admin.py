#encoding:utf-8
from django.contrib import admin
from UserInfo.models import UserInfo, DeliveryAddress

# Register your models here.
class UserInfoAdmin(admin.ModelAdmin):
    """定义用户信息管理页面"""
    list_display = ('pk', 'uName', 'uPwd', 'uEmail', 'isDeleted')
    search_fields = ['uName']

admin.site.register(UserInfo, UserInfoAdmin)

class DeliveryAddressAdmin(admin.ModelAdmin):
    """定义收件人信息管理页面"""
    list_display = ('pk', 'daOwner', 'daName', 'daPhone', 'daAddress', 'daPostCode')

admin.site.register(DeliveryAddress, DeliveryAddressAdmin)