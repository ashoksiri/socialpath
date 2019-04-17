from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from accounts import views as acc_views

app_name = "accounts"

urlpatterns = [
    url(r'^$', acc_views.home, name='index'),
    url(r'^home/$', acc_views.home, name='index'),
    url(r'^login/$', acc_views.login,name='login'),
    # url(r'^register/$', acc_views.register,name='register'),
    # url(r'^logout/$', acc_views.acc_logout,name='logout')
]