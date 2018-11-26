from django.conf.urls import url 
from . import views


urlpatterns = [	
	
	url(r'^coupons/$', views.coupon_apply, name='apply'),
]