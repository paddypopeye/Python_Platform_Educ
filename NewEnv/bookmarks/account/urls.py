from django.conf.urls import url, patterns
from django.conf import settings
from . import views


urlpatterns = [
# post views
#url(r'^login/$', views.user_login, name='login'),

# LOGIN/LOGOUT & EDIT URLS

url(r'^$', views.dashboard, name='dashboard'),
url(r'^users/follow/$', 'account.views.user_follow', name='user_follow'),
url(r'^users/$', 'account.views.user_list',name='user_list'),
url(r'^edit/$', 'account.views.edit', name='edit'),
url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
url(r'^logout/$', 'django.contrib.auth.views.logout', { 'template_name': 'registration/logout.html',}, name='logout' ),
url(r'^logout-then-login/$','django.contrib.auth.views.logout_then_login', name='logout_then_login'),
url(r'^users/(?P<username>[-\w]+)/$','account.views.user_detail',name='user_detail'),
# Change passowrds urls
url(r'^password-change/$', 'django.contrib.auth.views.password_change', name='password_change'),
url(r'^password-change/done/$', 'django.contrib.auth.views.password_change_done', name='password_change_done'),


# Restore passwords urls 
url(r'^password-reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
url(r'^password-reset/done/$','django.contrib.auth.views.password_reset_done', name='password_reset_done'),
url(r'^password-reset/complete/$','django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
	'django.contrib.auth.views.password_reset_confirm',name='password_reset_confirm'),

# Registration urls
url(r'^register/$', 'account.views.register', name='register'),


]


#          #url(r'^login/$', 'login', { 'template_name': 'registration/login.html'}, name='login' ),
#          #url(r'^logout/$', 'logout', { 'template_name': 'registration/logout.html', 'next_page':reverse('index') }, name='logout' ),
#  )