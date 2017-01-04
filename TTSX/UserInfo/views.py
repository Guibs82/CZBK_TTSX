from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from models import UserInfo
def postinfo(request):
    uname=request.POST['user_name']
    upaw=request.POST['cpwd']
    uemail=request.POST['email']
    login=UserInfo.create(uname,upaw,uemail)
    login.save()
    return render(request,'index.html')