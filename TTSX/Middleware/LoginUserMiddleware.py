#encoding:utf-8
from redis import StrictRedis

class LoginUserMiddleware(object):
    """中间件, 判定当前登入用户"""
    def process_request(self, request):
        """检测登入状态, 若未登入, 则跳转登录页面"""
        print request.path
        if request.path in ['/orderInfo/address/', '/orderInfo/', '/orderInfo/userInfo/', '/cartInfo/cartPage/', '/orderInfo/from_goods/']:
            # 创建StrictRedis 对象
            rs = StrictRedis(host='localhost', port=6379, db=0)
            # 检测用户cookie 中是否有session_id
            try:
                session_id = request.COOKIES['session_id']
            except Exception as e:
                session_id = ""
            if session_id == "":
                # 未登入
                from django.shortcuts import render, loader
                from django.http import HttpResponse
                t1 = loader.get_template('TTSX/UserInfo/login.html')
                response = HttpResponse(t1.render())
                aim_url = request.get_full_path()
                aim_url = aim_url.encode('utf-8')
                print '+++++'
                print aim_url
                print type(aim_url)
                print '+++++'
                response.set_cookie('aim_url', aim_url)
                return response