#encoding:utf-8
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from models import UserInfo
from hashlib import sha1
from redis import StrictRedis
import os

# Create your views here.

def getRegisterPage(request):
    """获取注册页面"""
    return render(request, 'TTSX/UserInfo/register.html')

@csrf_exempt
def checkUserExisted(reqest):
    """检测用户是否存在"""
    name2use = reqest.POST['name']
    nameList = UserInfo.objects.filter(uName=name2use)
    if len(nameList) == 1:
        checkResult = 1
    else:
        checkResult = 0

    from django.http import JsonResponse
    return JsonResponse({'checkResult': checkResult})

@csrf_exempt
def doRegister(request):
    """处理用户注册"""
    from UserInfo.models import UserInfo
    uname = request.POST['user_name']
    upwd = request.POST['pwd']
    uemail = request.POST['email']
    s1 = sha1()
    s1.update(upwd)
    upwd = s1.hexdigest()
    try:
        u = UserInfo(uName=uname, uEmail=uemail, uPwd=upwd)
        u.save()
    except Exception as e:
        print e.message
    from django.http import HttpResponse
    return HttpResponse('Ok')

def getLoginPage(request):
    """获取登录页面"""
    return render(request, 'TTSX/UserInfo/login.html')

@csrf_exempt
def doLogin(request):
    """处理登录
        To-Do:
            考虑抽取生成session_id 并写入cookies 的方法
    """
    username = request.POST['username']
    pwd = request.POST['pwd']
    remember = request.POST.getlist('remember') # [u'on'] --> 勾选后的返回结果 [] --> 未勾选返回的结果
    s1 = sha1()
    s1.update(pwd)
    pwd = s1.hexdigest()
    try:
        loginUser = UserInfo.objects.filter(uName=username, uPwd=pwd)
        if len(loginUser) == 0:
            # 登入失败, 用户名或密码错误
            # 跳转回登入页
            context = {}
            context['error_msg'] = '用户名或密码错误'
            return render(request, 'TTSX/UserInfo/login.html', context=context)
        else:
            # 登入成功
            # 创建StrictRedis 对象
            rs = StrictRedis(host='localhost', port=6379, db=0)
            # 检测用户cookie 中是否有session_id
            try:
                session_id = request.COOKIES['session_id']
            except Exception as e:
                session_id = ""
            if session_id == "":
                # cookies 中不存在session_id
                # 生成redis 中不存在的session_id, 作为本次会话在redis 中的的id
                session_id = filter(lambda x: not rs.exists(x), sha1(os.urandom(24)).hexdigest())
                # 本次session中要保存的数据字典
                session_msg = {}
                session_msg['username'] = loginUser[0].uName # 保存当前登录用户的用户名
                session_msg['user_pk'] = loginUser[0].pk # 保存当前登录用户的pk
                # rs.set(session_id, session_msg, ex=60*60*3) # 该session 信息有效时间3h
                # # 设置跳转到主页的response 对象
                # response = render_to_response('xxxxx.html')
                # # session_id 存入cookies
                # response.set_cookie('session_id', session_id, expires=60*60*3)
                # # 返回response 对象
                # return response

            else:
                # cookies 中存在session_id
                # 根据session_id 取出对象, 检测用户名是否一致, 若不一致, 则重建会话
                session_msg = eval(rs.get(session_id)) # 该session_id 在redis 中保存的session_msg 信息字典
                if not (session_msg['username'] == loginUser[0].uName): # 当前登入用户与redis 中该session_id 对应的用户不一致
                    # 重新创建session
                    # 生成redis 中不存在的session_id, 作为本次会话在redis 中的的id
                    session_id = filter(lambda x: not rs.exists(x), sha1(os.urandom(24)).hexdigest())
                    # 本次session中要保存的数据字典
                    session_msg = {}
                    session_msg['username'] = loginUser[0].uName  # 保存当前登录用户的用户名
                    # rs.set(session_id, session_msg, ex=60 * 60 * 3)  # 该session 信息有效时间3h
                    # # 设置跳转到主页的response 对象
                    # response = render_to_response('xxxxx.html')
                    # # 覆盖cookies 中的session_id
                    # response.set_cookie('session_id', session_id, expires=60 * 60 * 3)
                    # # 返回response 对象
                    # return response
                else:
                    # 同一个用户在时限内登入, 继续使用该session_id
                    pass

            # 在redis 和cookies 中写入session 相关信息
            rs.set(session_id, session_msg, ex=60 * 60 * 3)  # 该session 信息有效时间3h
            # 设置跳转到主页的response 对象

            # To-Do: 设定主页地址
            # response = render_to_response('xxxxx.html')

            # Test-Data:
            response = HttpResponse('Ok')

            # 覆盖cookies 中的session_id
            response.set_cookie('session_id', session_id, expires=60 * 60 * 3)
            # 根据remember选项, 若勾选, 则将用户名存入cookie
            if len(remember):
                # 用户名存入cookie
                response.set_cookie('username', loginUser[0].uName)
            # 返回response 对象
            return response

    except Exception as e:
        print '异常'
        print e.message
        # 出现异常
        # 跳转回登入页
        context = {}
        context['error_msg'] = '程序异常, 稍后再试'
        return render(request, 'TTSX/UserInfo/login.html', context=context)


def setC(request):
    response = HttpResponse('h')
    response.set_cookie('username', 'aaaaa')
    return response


















