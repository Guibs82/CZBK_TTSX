from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^list/(\d+)/(\d*)/?$',views.list,name='list'),
    url(r'^list1/(\d+)/(\d*)/?$',views.list1,name='list1'),
    url(r'^list2/(\d+)/(\d*)/?$',views.list2,name='list2'),
    url(r'^detail/$',views.detail,name='detail'),
]