from django.conf.urls import url
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^logout/$', views.Logout,name='logout'),
    url(r'^logout-then-login/$', auth_views.logout_then_login, name='logout_then_login'),
    url(r'^chat/', views.Home, name='home'),
    url(r'^post/$', views.Post, name='alpha/post'),
    url(r'^messages/$', views.Messages, name='alpha/messages'),
	
]

def __unicode__(self):
   return self.message	