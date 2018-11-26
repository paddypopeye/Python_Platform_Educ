from django.conf.urls import url
from . import views
from django.utils.translation import gettext_lazy as _
from django.views.decorators.cache import cache_page

urlpatterns = [
	url(_(r'^process/$'), cache_page(60*15)(views.payment_process), name='process'),
	url(_(r'^done/$'), cache_page(60*15)(views.payment_done), name='done'),
	url(_(r'^canceled/$'), cache_page(60*15)(views.payment_canceled), name='canceled'),
	]


	