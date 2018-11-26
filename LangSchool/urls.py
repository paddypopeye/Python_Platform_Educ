"""LangSchool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from __future__ import unicode_literals
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
sitemaps = {'posts': PostSitemap }

admin.autodiscover()

urlpatterns = [
    url(r'^chatpop/', include('chatpop.urls',namespace='chatpop', app_name='chatpop')),
    url(r'^auth/', include('djoser.urls')),
    url(r'^auth/', include('djoser.urls.authtoken')),
    #url(r'^chat/', include('jchat.urls')),
    #url(r'^fb_yomamabot/', include('fb_yomamabot.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('account.urls',namespace='account', app_name='account')),
    url(r'^alpha/', include('alpha.urls', namespace='alpha', app_name='alpha')),
    url(r'^api/',include('courses.api.urls', namespace='api')),
    url(r'^course/', include('courses.urls', namespace='courses', app_name='courses')),    
    url(r'^review/', include('blog.urls',namespace='blog',app_name='blog')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    url('social-auth/', include('social.apps.django_app.urls', namespace='social')),
    url(r'^images/', include('images.urls', namespace='images', app_name='images')),
    url(r'^rosetta/',include('rosetta.urls')),
    url(r'^orders/', include('orders.urls', namespace='orders')),
    url(r'^cart/', include('cart.urls', namespace='cart')),
    url(r'^payment/',include('payment.urls', namespace='payment')),
    url(r'^paypal/', include('paypal.standard.ipn.urls')),
    url(r'^coupons/',include('coupons.urls', namespace='coupons')),
    url(r'^students/', include('students.urls', namespace='students')),
    url(r'^friendship/', include('friendship.urls')),
    url(r'^shop/', include('shop.urls', namespace='shop')),
]

urlpatterns = i18n_patterns(
        url(r'^chatpop/', include('chatpop.urls',namespace='chatpop', app_name='chatpop')),
        url(r'^auth/', include('djoser.urls')),
        url(r'^auth/', include('djoser.urls.authtoken')),
        url(_(r'^alpha/'), include('alpha.urls', namespace='alpha', app_name='alpha')),
        #url(r'^chat/', include('jchat.urls')),
        url(r'^admin/', include(admin.site.urls)),
        url(_(r'^'), include('account.urls',namespace='account', app_name='account')),
        url(r'^api/',include('courses.api.urls', namespace='api')),
        url(_(r'^course/'), include('courses.urls', namespace='courses', app_name='courses')),
        url(_(r'^review/'), include('blog.urls',namespace='blog',app_name='blog')),
        url('social-auth/', include('social.apps.django_app.urls', namespace='social')),
        url(_(r'^images/'), include('images.urls', namespace='images', app_name='images')),
        url(_(r'^cart/'), include('cart.urls', namespace='cart')),
        url(_(r'^orders/'), include('orders.urls', namespace='orders')),
        url(_(r'^payment/'), include('payment.urls',namespace='payment')),
        url(r'^paypal/', include('paypal.standard.ipn.urls')),
        url(_(r'^coupons/'), include('coupons.urls',namespace='coupons')),
        url(r'^rosetta/', include('rosetta.urls')),
        url(_(r'^students/'), include('students.urls', namespace='students')),
        url(_(r'^shop/'), include('shop.urls', namespace='shop')),
)   

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        url(r'^rosetta/', include('rosetta.urls'))
]
 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)