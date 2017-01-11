#encoding:utf-8
from django.contrib import admin
from OrderInfo.models import OrderInfo, OrderDetailInfo

# Register your models here.
class OrderInfoAdmin(admin.ModelAdmin):
    """定义订单信息管理页面"""
    list_display = ('pk', 'oUser', 'oTotal', 'oTime', 'oState')
    search_fields = ['gTitle']

admin.site.register(OrderInfo, OrderInfoAdmin)

class OrderDetailInfoAdmin(admin.ModelAdmin):
    """定义订单详细信息管理"""
    list_display = ('pk', 'oiOrder', 'oiGoods', 'oiCount', 'oiPrice')
    search_fields = ['oiOrder']

admin.site.register(OrderDetailInfo, OrderDetailInfoAdmin)