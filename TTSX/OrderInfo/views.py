#coding=utf-8
from django.shortcuts import render,redirect
from django.http import HttpResponse
from models import *
from django.http import JsonResponse 
from django.core.paginator import Paginator	
from UserInfo.models import *
from GoodsInfo.models import *
from CartInfo.models import *
from django.views.decorators.csrf import csrf_exempt
from Tools.SessionTools import getUserPk

def index(request,pd=1):
	pageName = '用户中心'
	num=int(pd)
	#获取用户信息
	user_pk = getUserPk(request)
	#分页
	data = OrderInfo.objects.filter(oUser=user_pk)
	p = Paginator(data,2)
	alist=p.page_range
	#提出第一页（默认页）
	numlist = p.page_range[1:]
	max_num = int(alist[-1])
	#判断最大页数
	if num >= max_num:
		num = max_num		
	tex = p.page(num)
	#每页最多显示两个订单，接收每个订单的商品对象列表
	context = {'key2':numlist,'key':tex,'key1':num,'pageName':pageName}
	return render(request,'TTSX/OrderInfo/index.html',context)

def jax(request,num=1):
	num_page=int(num)
	user_pk = getUserPk(request)
	data = OrderInfo.objects.filter(oUser=user_pk)
	p = Paginator(data,2)
	tex = p.page(num_page)
	mylist = []
	for temp in tex:
		goods_obj=OrderDetailInfo.objects.filter(oiOrder=temp.id)
		mylist1=[]
		for temp1 in goods_obj:
			mylist1.append([temp1.oiGoods.gImage,temp1.oiGoods.gTitle,temp1.oiCount,temp1.oiPrice])
		mylist.append([temp.id,mylist1])
		print temp.id
	return JsonResponse({'mylist':mylist})

def buy(request,pd):
	Order = OrderInfo.objects.filter(id = pd)
	#用户的id是用户地址的外键，从而得到此用户的所有的地址
	address = DeliveryAddress.objects.filter(daOwner=int(1))
	#大订单的id是所有商品订单的外键，从而得到此订单下的所有商品对象
	goods_data = OrderDetailInfo.objects.filter(oiOrder=int(pd))
	num1 = len(goods_data)
	mylist = []
	for temp in goods_data:
		nums=str(float(temp.oiPrice)*int(temp.oiCount))+'元'
		mylist.append((nums,temp))
	#将对象放到元组里，能使用。以字典的形式，不好取
	context = {'key':mylist,'address':address[0],'Order':Order[0],'num1':num1,'d':pd}
	return render(request,'TTSX/OrderInfo/buy.html',context)

def from_goods(request):
	#获取点击结算来的参数
	print 'from_goods'
	t1 = request.GET['t1']
	p1 = request.GET['p1']
	c1 = request.GET['c1']
	#找出当前用户对象
	user_pk = getUserPk(request)
	u1 = UserInfo.objects.filter(id =user_pk)[0]
	total = int(c1)*float(p1)
	numstr = str(total)+'元'
	#找出相应的商品对象
	goods1=GoodsInfo.objects.filter(id=int(t1))[0]
	#添加订单，默认为未支付状态，oUser必须赋值为一个对象
	od = OrderInfo.objects.create(oUser=u1,oTotal=total,oState=1)
	od.save()
	#添加订单中的商品信息
	og=OrderDetailInfo.objects.create(oiOrder=od,oiGoods=goods1,oiCount=int(c1),oiPrice=float(p1))
	og.save()
	#添加收货地址
	address = DeliveryAddress.objects.filter(daOwner=u1)
	mylist=[(numstr,og)]
	context = {'key':mylist,'address':address[0],'Order':od,'num1':1,'d':od.id}
	return render(request,'TTSX/OrderInfo/buy.html',context)
	return HttpResponse('123')

def from_chart(request):
	print 'from_chart'
	t1 = request.GET.getlist('t1')
	p1 = request.GET.getlist('p1')
	c1 = request.GET.getlist('c1')
	Num=len(t1)
	print t1
	#计算订单总价格
	total=0
	i=0
	for temp in p1:
		total+=float(temp)*int(c1[i])
		i+=1
	user_pk = getUserPk(request)
	u1 = UserInfo.objects.filter(id=user_pk)[0]
	#添加订单，默认为未支付状态，oUser必须赋值为一个对象
	od = OrderInfo.objects.create(oUser=u1,oTotal=total,oState=1)
	od.save()
	mylist=[]
	j=0
	for temp in t1:
		#找出相应的商品对象
		cart=CartInfo.objects.filter(id=int(temp))[0]
		goods1 = cart.cGoods
		totals=float(p1[j])*int(c1[j])
		total_str=str(totals)+'元'		
		#添加订单中的商品信息
		og=OrderDetailInfo.objects.create(oiOrder=od,oiGoods=goods1,oiCount=int(c1[j]),oiPrice=float(p1[j]))
		og.save()
		mylist.append((total_str,og))
		j+=1
	#添加收货地址
	user_pk = getUserPk(request)
	user_obj = UserInfo.objects.filter(pk=user_pk)[0]
	address = DeliveryAddress.objects.filter(daOwner=user_obj)
	context = {'key':mylist,'address':address[0],'Order':od,'num1':Num,'d':od.id}
	return render(request,'TTSX/OrderInfo/buy.html',context)

#用户中心页面跳转
def address(request):
	#返回地址页面
	pageName = '用户中心'
	context={'pageName':pageName}
	return render(request,'TTSX/OrderInfo/address.html',context)

def turn(request,num):
	#结算成功，更改订单状态，并返回用户订单页面
	OrderInfo.objects.filter(id=num).update(oState=0)
	#过滤出订单中的所有商品信息，清空购物车的商品，未用数据尝试
	good_obj = OrderDetailInfo.objects.filter(oiOrder=num)
	for temp in good_obj:
		#购物车的cGoods这个外键字段与订单中的外键字段相对应
		CartInfo.objects.filter(cGoods=temp.oiGoods).delete()
	return redirect('/orderInfo/')

def user_addr(request):
	#获取当前登陆用户
	user_pk = getUserPk(request)
	u1 = UserInfo.objects.filter(id=user_pk)[0]
	#获取当前用户的所有的收货地址
	addrList = DeliveryAddress.objects.filter(daOwner=u1)
	mylist=[]
	for temp in addrList:
		mylist.append([temp.daName,temp.daAddress,temp.daPhone,temp.daPostCode])
	return JsonResponse({'key':mylist})

@csrf_exempt
def from_usercenter(request):
	#获取表单数据
	Name = request.POST['postName']
	Area = request.POST['postAddress']
	Code = request.POST['postCode']
	Num = request.POST['postNum']
	#获取当前登陆用户
	user_pk = getUserPk(request)
	u1 = UserInfo.objects.filter(id=user_pk)[0]
	#添加订单，默认为未支付状态，oUser必须赋值为一个对象
	addr= DeliveryAddress.objects.create(daOwner=u1,daName=Name,daPhone=Num,daAddress=Area,daPostCode=Code)
	addr.save()
	#render一个新页面，页面加载过程中触发ajax请求
	pageName = '用户中心'
	context={'pageName':pageName}
	return render(request,'TTSX/OrderInfo/address.html',context)

def userInfo(request):
	#用户信息页面
	pageName = '用户中心'
	context={'pageName':pageName}
	return render(request,'TTSX/OrderInfo/userInfo.html',context)

def userDetailInfo(request):
	#ajax向用户信息页面加载信息
	user_pk = getUserPk(request)
	user_obj = UserInfo.objects.filter(pk=user_pk)
	addr1 = DeliveryAddress.objects.filter(daOwner=user_obj)[0]
	addr_list = [addr1.daName,addr1.daPhone,addr1.daAddress]
	return JsonResponse({'key':addr_list})










