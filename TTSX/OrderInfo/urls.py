from django.conf.urls import url
import views

urlpatterns = [
	url(r'^$',views.index),
	url(r'^(\d+)/$',views.index),
	url(r'^jax/(\d+)/$',views.jax),
	url(r'^buy/(\d+)/$',views.buy),
	url(r'^address/$',views.address),
	url(r'^userInfo/$',views.userInfo),
	url(r'^done/(\d+)/$',views.turn),
	url(r'^from_goods/$',views.from_goods),
	url(r'^from_cart/$',views.from_chart),
	url(r'^from_usercenter/$',views.from_usercenter),
	url(r'^user_addr/$',views.user_addr),
	url(r'^userDetailInfo/$',views.userDetailInfo),
]