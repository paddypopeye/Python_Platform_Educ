from django.conf.urls import url 
from . import views
from django.utils.translation import gettext_lazy as _
from django.views.decorators.cache import cache_page
urlpatterns = [	
	url(_(r'^create/$'), cache_page(60*15)(views.order_create), name='order_create'),
	url(r'^admin/order/(?P<order_id>\d+)/$', cache_page(60*15)(views.admin_order_detail), name='admin_order_detail'),
	url(r'^admin/order/(?P<order_id>\d+)/pdf/$', cache_page(60*15)(views.admin_order_pdf), name='admin_order_pdf'),
	]