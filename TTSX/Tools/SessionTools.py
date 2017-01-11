#encoding:utf-8
def getUserPk(request):
    """获取用户pk"""
    from redis import StrictRedis
    # 创建StrictRedis 对象
    rs = StrictRedis(host='localhost', port=6379, db=0)
    # 检测用户cookie 中是否有session_id
    try:
        session_id = request.COOKIES['session_id']
        session_dir = eval(rs.get(session_id))
        user_pk = session_dir['user_pk']
        return user_pk
    except Exception as e:
        print e.message

def getCartCount(request):
    try:
        user_pk = getUserPk(request)
        from UserInfo.models import UserInfo
        user_obj = UserInfo.objects.filter(pk=user_pk)[0]
        from CartInfo.models import CartInfo
        cartList = CartInfo.objects.filter(cUser=user_obj)
        return len(cartList)
    except Exception as e:
        print e.message
        return 0