from django.contrib.auth import views as auth_views 
from django.conf.urls import include, url
from . import views
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.views.decorators.cache import cache_page
from django.contrib.auth.decorators import login_required
urlpatterns = [
	url(_(r'^clogin/$'), views.teacher_login, name='clogin'),
	url(_(r'^clogout/$'),auth_views.logout,{'template_name': '../templates/registration/coursesloggedout.html'}, name='clogout'),
	url(_(r'^clogout-then-clogin/$'), auth_views.logout_then_login, name='logout_then_login'),
	url(_(r'^mine/$'), login_required(views.ManageCourseListView.as_view()),name='manage_course_list'),
	url(_(r'^create/$'), cache_page(60*3)(login_required(views.CourseCreateView.as_view())), name='course_create'),
	url(_(r'^(?P<pk>\d+)/edit/$'), cache_page(60*3)(views.CourseUpdateView.as_view()), name='course_edit'),
	url(_(r'^(?P<pk>\d+)/delete/$'), cache_page(60*3)(views.CourseDeleteView.as_view()), name='course_delete'),
	url(_(r'^(?P<pk>\d+)/module/$'), cache_page(60*3)(views.CourseModuleUpdateView.as_view()), name='course_module_update'),
	url(_(r'^module/(?P<module_id>\d+)/content/(?P<model_name>\w+)/create/$'), cache_page(60*15)(views.ContentCreateUpdateView.as_view()), name='module_content_create'),
	url(_(r'^module/(?P<module_id>\d+)/content/(?P<model_name>\w+)/(?P<id>\d+)/$'), cache_page(60*15)(views.ContentCreateUpdateView.as_view()), name='module_content_update'),
	url(_(r'^module/(?P<module_id>\d+)/$'), cache_page(60*1)(views.ModuleContentListView.as_view()), name='module_content_list'),
	url(_(r'^content/(?P<id>\d+)/delete/$'), cache_page(60*1)(views.ContentDeleteView.as_view()),name='module_content_delete'),
	url(_(r'^module/order/$'),cache_page(60*5)(views.ModuleOrderView.as_view()),name='module_order'),
	url(_(r'^content/order/$'),cache_page(60*5)(views.ContentOrderView.as_view()),name='content_order'),
	url(_(r'^list/$'), cache_page(60*1)(views.CourseListView.as_view()), name='course_list'),
	url(_(r'^subject/(?P<subject>[\w-]+)/$'), cache_page(60*1)(views.CourseListView.as_view()), name='course_list_subject'),
	url(_(r'^(?P<slug>[\w-]+)/$'), cache_page(60*1)(views.CourseDetailView.as_view()), name='course_detail'),
]