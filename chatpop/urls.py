from django.conf.urls import url
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^chat/', views.Home, name='home'),
    url(r'^post/$', views.Post, name='chatpop/post'),
    url(r'^messages/$', views.Messages, name='chatpop/messages'),
	
]

def __unicode__(self):
   return self.message	