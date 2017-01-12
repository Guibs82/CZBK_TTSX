from django.conf.urls import url
import views

urlpatterns = [
    url(r'^cartPage/$', views.getCartPage),
    url(r'^changeCount/$', views.changeCount),
    url(r'^delCartInfo/$', views.delCartInfo),
    url(r'^addCartInfo/$', views.addCartInfo),
    url(r'^getCartCount/$', views.getCartCount),
    # url(r'^testPage/$', views.getTestPage),
]

# 2 2 2 10