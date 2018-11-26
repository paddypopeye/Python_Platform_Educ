from django.conf.urls import url
from . import views
from django.views.decorators.cache import cache_page
from django.utils.translation import gettext_lazy as _


urlpatterns = [
	url(_(r'^list/$'), views.product_list, name='product_list'),
	url(_(r'^(?P<category_slug>[-\w]+)/$'), views.product_list, name='product_list_by_category'),
	url(_(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$'), views.product_detail, name='product_detail'),
]