from django.conf.urls import url
from . import views
from django.views.decorators.cache import cache_page
from django.utils.translation import gettext_lazy as _
urlpatterns = [
	url(_(r'^create/$'),cache_page(30*1)(views.image_create	), name='create'),
	url(_(r'^detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$'),views.image_detail, name='detail'),
	url(_(r'^like/$'),views.image_like, name='like'),
	url(r'^$', cache_page(30*1)(views.image_list), name='list'),
	url(_(r'^ranking/$'),cache_page(30*1)(views.image_ranking), name='create_rank'),
]