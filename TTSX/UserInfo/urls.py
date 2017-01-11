from django.conf.urls import url
import views

urlpatterns = [
    url(r'^registerPage/$', views.getRegisterPage),
    url(r'^userExisted/$', views.checkUserExisted),
    url(r'^doRegister/$', views.doRegister),

    url(r'^loginPage/$', views.getLoginPage),
    url(r'^doLogin/$', views.doLogin),
]