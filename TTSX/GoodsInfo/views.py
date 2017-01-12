#coding=utf-8
from django.shortcuts import render, redirect
from models import *
from django.core.paginator import  *
from django.core.paginator import Paginator
from Tools.SessionTools import *
# Create your views here.
def index(request):
    fruit = GoodsInfo.objects.filter(gType=1)
    seafood = GoodsInfo.objects.all().filter(gType=2)
    meat = GoodsInfo.objects.all().filter(gType=3)
    eggs  =  GoodsInfo.objects.all().filter(gType=4)
    vegetables = GoodsInfo.objects.all().filter(gType=5)
    ice = GoodsInfo.objects.all().filter(gType=6)
    ftype = TypeInfo.objects.filter(pk=1)
    stype = TypeInfo.objects.filter(pk=2)
    mtype = TypeInfo.objects.filter(pk=3)
    etype = TypeInfo.objects.filter(pk=4)
    vtype = TypeInfo.objects.filter(pk=5)
    itype = TypeInfo.objects.filter(pk=6)
    cart_count = getCartCount(request)
    context = {'fruit':fruit[0:4],'meat':meat[0:4],
               'seafood':seafood[0:4],'eggs':eggs[0:4],
               'vegetables': vegetables[0:4], 'ice': ice[0:4],
               'ftype':ftype,'stype':stype,'vtype':vtype,'mtype':mtype,'etype':etype,
               'itype':itype,
               'cart_count':cart_count}
    return render(request,'TTSX/index.html',context)


def list(request,tid,pIndex):

    list = GoodsInfo.objects.all().filter(gType=tid)
    list1 = list[0].gType.id

    len1 = len(list)
    if len1 > 2:
        len2 = len1 - 2
        list_1 = list[len2:]
    else:
        list_1 = list

    if pIndex == '':
        pIndex = '1'

    paginator = Paginator(list,10)
    pcount = paginator.num_pages
    pIndex = int(pIndex)
    page = paginator.page(pIndex)
    page_num = paginator.page_range
    pPrev = pIndex
    pNext = pIndex
    if page.has_previous():
        pPrev = pIndex - 1
    if page.has_next():
        pNext = pIndex + 1
    cart_count = getCartCount(request)
    context = {'list': list,'list_1':list_1,'page':page,'page_num':page_num,'pPrev':pPrev,'pNext':pNext,'pIndex':pIndex,'pcount':pcount,
               'list1':list1, 'cart_count':cart_count}
    return render(request,'TTSX/list.html',context)


def list1(request,tid,pIndex):
    list = GoodsInfo.objects.all().filter(gType=tid).order_by('gPrice')
    list1 = list[0].gType.id
    len1 = len(list)
    if len1 > 2 :
        len2 = len1 - 2
        list_1 = list[len2:]
    else:
        list_1 = list

    if pIndex == '':
        pIndex = '1'

    paginator = Paginator(list,10)
    pcount = paginator.num_pages
    pIndex = int(pIndex)
    page = paginator.page(pIndex)
    page_num = paginator.page_range
    pPrev = pIndex
    pNext = pIndex
    if page.has_previous():
        pPrev = pIndex - 1
    if page.has_next():
        pNext = pIndex + 1
    cart_count = getCartCount(request)
    context = {'list': list,'list_1':list_1,'page':page,'page_num':page_num,'pPrev':pPrev,'pNext':pNext,'pIndex':pIndex,'pcount':pcount,
               'list1':list1, 'cart_count': cart_count}
    return render(request,'TTSX/list1.html',context)


def list2(request,tid,pIndex):
    list = GoodsInfo.objects.all().filter(gType=tid).order_by('-gPrice')
    list1 = list[0].gType.id
    len1 = len(list)
    if len1 > 2:
        len2 = len1 - 2
        list_1 = list[len2:]
    else:
        list_1 = list

    if pIndex == '':
        pIndex = '1'

    paginator = Paginator(list,10)
    pcount = paginator.num_pages
    pIndex = int(pIndex)
    page = paginator.page(pIndex)
    page_num = paginator.page_range
    pPrev = pIndex
    pNext = pIndex
    if page.has_previous():
        pPrev = pIndex - 1
    if page.has_next():
        pNext = pIndex + 1
    cart_count = getCartCount(request)
    context = {'list': list,'list_1':list_1,'page':page,'page_num':page_num,'pPrev':pPrev,'pNext':pNext,'pIndex':pIndex,'pcount':pcount,
               'list1':list1, 'cart_count':cart_count}
    return render(request,'TTSX/list2.html',context)


def detail(request):
    id = request.GET['id']
    goods = GoodsInfo.objects.filter(pk=id)
    price = goods[0].gPrice
    goods_t = goods[0].gType.id
    goods_1 = GoodsInfo.objects.filter(gType=goods_t)
    len1 = len(goods_1)
    print len1
    if len1 > 2:
        len2 = len1 - 2
        print len2
        goods_1 = goods_1[len2:]
    else:
        goods_1 = goods_1
    user_pk = getUserPk(request)
    cart_count = getCartCount(request)
    context = {'goods':goods,'goods_1':goods_1,'id':id,'user_pk':user_pk,'price':price, 'cart_count':cart_count}
    return render(request,'TTSX/detail.html',context)


