"""bookmarks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls import static
from django.contrib.auth import views as auth_views



urlpatterns = [
   
    url(r'^cart/', include('cart.urls', namespace='cart')), 
    url(r'^account/', include("account.urls",)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^course/', include('courses.urls',)),
    #url(r'^rosetta/', include('rosetta.urls')),
    url(r'^orders/', include('orders.urls', namespace='orders')),
    url(r'^images/', include('images.urls', namespace='images')),
    url(r'^coupons/', include('coupons.urls', namespace='coupons')),
    url(r'^products/', include("shop.urls",namespace='shop')),
    url(r'^payment/', include('payment.urls', namespace='payment')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^paypal/', include('paypal.standard.ipn.urls')),
    

]

if settings.DEBUG:
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),)



