#encoding:utf-8
from django.shortcuts import render
from CartInfo.models import CartInfo
from UserInfo.models import UserInfo
from GoodsInfo.models import GoodsInfo
from redis import StrictRedis
from django.views.decorators.csrf import csrf_exempt
from Tools.SessionTools import getUserPk

# Create your views here.
def getCartPage(request):
    """返回购物车页面"""
    context = {}
    context['pageName'] = '购物车'

    try:
        session_id = request.COOKIES['session_id']
    except Exception as e:
        session_id = ""

    if session_id != "":
        # get 到了session_id
        rs = StrictRedis(host='localhost', port=6379, db=0)
        session_msg = eval(rs.get(session_id))
        user_pk = session_msg['user_pk']
        cartInfoes = CartInfo.objects.filter(cUser_id=user_pk)
        context['cartInfoes'] = cartInfoes

    return render(request, 'TTSX/CartInfo/cart.html', context=context)

@csrf_exempt
def changeCount(request):
    """处理Ajax请求, 更改数据库中的商品数量"""
    cpk = request.POST['cart_pk']
    count = request.POST['count']
    try:
        cart_info = CartInfo.objects.get(pk=cpk)
        cart_info.cCount = count
        cart_info.save()
        updated_count = CartInfo.objects.get(pk=cpk).cCount
    except Exception as e:
        print e.message

    from django.http import JsonResponse
    return JsonResponse({'updatedCount': updated_count, 'cpk': cpk})

@csrf_exempt
def delCartInfo(request):
    """处理Ajax请求, 删除购物车记录"""
    cpk = request.POST['cart_pk']
    delResult = 0
    try:
        cart_info = CartInfo.objects.get(pk=cpk)
        cart_info.delete()
        delResult = 1
    except Exception as e:
        print e.message

    from django.http import JsonResponse
    return JsonResponse({'delResult': delResult})

@csrf_exempt
def addCartInfo(request):
    """增加购物车记录
        拿到的数据
            good_pk
            user_pk
            count
    """
    good_pk = request.POST['good_pk']
    # user_pk = request.POST['user_pk']
    user_pk = getUserPk(request)
    count = request.POST['count']

    addResult = 0

    cartInfoList = CartInfo.objects.filter(cGoods=GoodsInfo.objects.filter(pk=good_pk), cUser=UserInfo.objects.filter(pk=user_pk))
    if len(cartInfoList) == 1:
        # 该用户的购物车已有该商品
        try:
            cartInfoList[0].cCount = int(cartInfoList[0].cCount) + int(count)
            cartInfoList[0].save()
            print cartInfoList[0].cCount
            addResult = 1
        except Exception as e:
            print e.message
    else:
        # 当前用户没有该商品
        try:
            cartInfo = CartInfo(cGoods=GoodsInfo.objects.filter(pk=good_pk)[0], cUser=UserInfo.objects.filter(pk=user_pk)[0], cCount=count)
            cartInfo.save()
            addResult = 1
        except Exception as e:
            print e.message

    cart_count = len(CartInfo.objects.filter(cUser=UserInfo.objects.filter(pk=user_pk)[0]))

    from django.http import JsonResponse
    return JsonResponse({'addResult': addResult, 'cart_count': cart_count})


# @csrf_exempt
# def getTestPage(request):
#     """测试添加购物车信息页面"""
#     session_id = request.COOKIES['session_id']
#     from redis import StrictRedis
#     rs = StrictRedis()
#     s_dic = eval(rs.get(session_id))
#     user_pk = s_dic['user_pk']
#
#
#     return render(request, 'TTSX/GoodsInfo/addCartInfo.html', context={'user_pk': user_pk})