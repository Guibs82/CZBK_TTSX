#encoding:utf-8
from django.contrib import admin
from GoodsInfo.models import GoodsInfo, TypeInfo

# Register your models here.
class GoodsInfoAdmin(admin.ModelAdmin):
    """定义商品信息管理页面"""
    list_display = ('pk', 'gTitle', 'gType', 'gImage', 'gPrice', 'gDesc', 'isDeleted')
    search_fields = ['gTitle']

admin.site.register(GoodsInfo, GoodsInfoAdmin)

class TypeInfoAdmin(admin.ModelAdmin):
    """定义商品类别信息管理页面"""
    list_display = ('pk', 'tTitle', 'isDeleted')
    search_fields = ['tTitle']

admin.site.register(TypeInfo, TypeInfoAdmin)