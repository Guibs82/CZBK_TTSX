#encoding:utf-8
from redis import StrictRedis

class LoginUserMiddleware(object):
    """中间件, 判定当前登入用户"""
    def process_request(self, request):
        """检测登入状态, 若未登入, 则跳转登录页面"""
        if request.path not in ['/goodsInfo/index/', '/userInfo/loginPage/', '/userInfo/registerPage/', '/userInfo/doLogin/',
                                '/userInfo/doRegister/']:
            # 创建StrictRedis 对象
            rs = StrictRedis(host='localhost', port=6379, db=0)
            # 检测用户cookie 中是否有session_id
            try:
                session_id = request.COOKIES['session_id']
            except Exception as e:
                session_id = ""
            if session_id == "":
                # 未登入
                from django.shortcuts import render
                return render(request, 'TTSX/UserInfo/login.html')