from django.conf.urls import url, include
from rest_framework import routers
from . import views
from django.views.decorators.cache import cache_page
router = routers.DefaultRouter()
router.register('courses', views.CourseViewSet)

urlpatterns = [
	url(r'^', include(router.urls)),
	url(r'^subjects/$', cache_page(60*1)(views.SubjectListView.as_view()), name='subject_list'),
	url(r'^subjects/(?P<pk>\d+)/$', cache_page(60*1)(views.SubjectDetailView.as_view()), name='subject_detail'),
	#url(r'^courses/(?P<pk>\d+)/enroll/$', cache_page(60*15)(views.CourseEnrollView.as_view()), name='course_enroll'),
]