#encoding:utf-8
from django.shortcuts import render
from CartInfo.models import CartInfo
from redis import StrictRedis

# Create your views here.
def getCartPage(request):
    """返回购物车页面"""
    context = {}
    context['pageName'] = '购物车'

    # To-Do:
    #   返回当前用户的购物车对象
    # 1. 获得cookies 中的session_id
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