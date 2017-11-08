from django.conf.urls import url
from images import views


urlpatterns = [
           url(r'^ranking/$', 'images.views.image_ranking', name='create'),
           url(r'^$', 'images.views.image_list', name='list'),
           url(r'^like/$', 'images.views.image_like', name='like'),
           url(r'^detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$', 'images.views.image_detail', name='detail'),
           url(r'^create/$', 'images.views.image_create', name='create'),
           ]

