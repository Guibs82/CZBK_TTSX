#encoding:utf-8
from django.contrib import admin
from CartInfo.models import CartInfo

# Register your models here.
class CartInfoAdmin(admin.ModelAdmin):
    """定义购物车信息管理页面"""
    list_display = ('pk', 'cUser', 'cGoods', 'cCount')

admin.site.register(CartInfo, CartInfoAdmin)
