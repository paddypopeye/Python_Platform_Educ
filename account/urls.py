from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views
from django.views.decorators.cache import cache_page
from django.utils.translation import gettext_lazy as _
urlpatterns = [
	#url(r'^login/$', views.user_login, name='login'),
	url(_(r'^connect/(?P<pk>\d+)/$'), views.request_friends, name='friends'),
	url(_(r'^accept/(?P<pk>\d+)/$'), views.acceptRequest, name='accept_request'),
	url(_(r'^reject/(?P<pk>\d+)/$'), views.rejectRequest, name='reject_request'),
	url(r'^remove/(?P<pk>\d+)/$', views.removeFriend, name='removeFriend'),
	url(_(r'^login/$'), auth_views.login, name='login'),
	url(_(r'^logout/$'), auth_views.logout, { 'template_name': 'registration/logout.html',}, name='logout'),
	url(_(r'^logout-then-login/$'), auth_views.logout_then_login, name='logout_then_login'),
	url(r'^$', views.dashboard, name='dashboard'),
	url(_(r'^password-change/done/$'), cache_page(60*2)(auth_views.password_change_done), { 'template_name': 'registration/password_change_done.html',},name='password_change_done'),
	url(_(r'^password-change/$'), cache_page(60*2)(auth_views.password_change), {'template_name': 'registration/password_change_form.html', 'post_change_redirect': 'account:password_change_done'}, name='password_change'),
	url(_(r'^password-reset/$'),cache_page(60*2)(auth_views.password_reset),{'template_name': 'registration/password_reset_form.html', 'post_reset_redirect': 'account:password_reset_done'}, name='password_reset'),
	url(_(r'^password-reset/done/$'),cache_page(60*2)(auth_views.password_reset_done),name='password_reset_done'),
	url(_(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$'), cache_page(60*2)(auth_views.password_reset_confirm),{'template_name': 'registration/password_reset_confirm.html', 'post_reset_redirect': 'account:password_reset_complete'}, name='password_reset_confirm'),
	url(_(r'^password-reset/complete/$'), cache_page(60*1)(auth_views.password_reset_complete), name='password_reset_complete'),
	url(_(r'^users/follow/$'), views.user_follow, name='user_follow'),
	url(_(r'^users/$'), views.user_list,name='user_list'),
	url(_(r'^users/(?P<username>[-\w]+)/$'), views.user_detail, name='user_detail'),
	url(_(r'^register/$'), cache_page(60*1)(views.register), name='register'),
	url(_(r'^edit/$'), cache_page(60*1)(views.edit), name='edit'), 
	]