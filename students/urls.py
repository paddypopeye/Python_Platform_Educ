from django.conf.urls import url
from . import views
from django.views.decorators.cache import cache_page
from django.utils.translation import gettext_lazy as _


urlpatterns = [

	url(_(r'^register/$'), cache_page(60*1)(views.StudentRegistrationView.as_view()), name='student_registration'),
	url(_(r'^enroll-course/$'),cache_page(60*1)(views.StudentEnrollCourseView.as_view()), name='student_enroll_course'),
	url(_(r'^courses/$'),cache_page(60*1)(views.StudentCourseListView.as_view()), name='student_course_list'),
	url(_(r'^course/(?P<pk>\d+)/$'), cache_page(60*1)(views.StudentCourseDetailView.as_view()),name='student_course_detail'),
	url(_(r'^course/(?P<pk>\d+)/(?P<module_id>\d+)/$'),cache_page(60*1)(views.StudentCourseDetailView.as_view()),name='student_course_detail_module'),


	]