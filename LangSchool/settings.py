"""
Django settings for LangSchool project.

Generated by 'django-admin startproject' using Django 1.11.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
# -*- coding: utf-8 -*-
import os
from django.utils.encoding import force_unicode
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.conf import settings
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'nd9m3=4wdji&rcenisdrj#vsrnfcju^x093*)hp%%+^z5n6rxg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['192.168.10.10', u'langschool.com']

CACHES = {
    'default': {
    'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache','LOCATION': '192.168.10.10:11211',
    }
}


# Application definition

INSTALLED_APPS = [
    'account',
    'actions',
    'alpha',
    'blog',
    'cart',
    'chatpop',
    'coupons',
    'courses',
    'embed_video',
    'friendship',
    'haystack',
    'images',
    'memcache_status',
    'orders',
    'parler',
    'payment',
    'paypal.standard.ipn',
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',
    'rosetta',
    'shop',
    'students',
    #'social.apps.django_app.default',
    'sorl.thumbnail',
    'taggit',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    
]

SITE_ID = 4
ROOT_URLCONF = 'LangSchool.urls'
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'LangSchool.middleware.OnlineNowMiddleware',
]



TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart',
                'account.context_processor.friendsProcessor',
                
            ],
        },
    },
]

WSGI_APPLICATION = 'LangSchool.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'langschool',
        'USER': 'vagrant',
        'PASSWORD': 'vagrant1',
        'HOST': '192.168.10.10',
        'PORT': '',
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/
DEFAULT_CHARSET='utf-8'
ROSETTA_STORAGE_CLASS = 'rosetta.storage.CacheRosettaStorage' 
FILE_CHARSET='utf-8'
DEFAULT_CONTENT_TYPE='text/html'
LANGUAGE_CODE = 'en'
LANGUAGES = (

    ('en',_('english')),
    ('ca',_('catalan')),
    ('es', _('spanish')),

)

LOCALE_PATHS = (
        os.path.join(BASE_DIR, 'locale/'),
    )
PROJECT_PATH = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]

PARLER_LANGUAGES = {
    4: (
        {'code': 'en',},
        {'code': 'es',},
        {'code': 'ca'},
),

'default': {
    'fallback': 'en',
    'hide_untranslated': False,
    }
}
TIME_ZONE = 'Europe/Madrid'

USE_I18N = True
USE_L10N = True
USE_TZ = True
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATIC_DIRS = [os.path.join(BASE_DIR, 'static/js/'),os.path.join(BASE_DIR, 'static/css/')]

#HAYSTACK INFO
HAYSTACK_CONNECTIONS = {
    'default':{
    'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
    'URL': 'http://192.168.10.10:8983/solr/blog'
    },
}

#SMTP
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'eugenesleator17@gmail.com'
EMAIL_HOST_PASSWORD = 'Password001'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

LOGIN_REDIRECT_URL = reverse_lazy('account:dashboard')
LOGIN_URL = reverse_lazy('account:login')
LOGOUT_URL = reverse_lazy('account:logout')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEIDA_DIRS = [
    os.path.join(BASE_DIR,'media/users/'),
]

AUTHENTICATION_BACKENDS = (
        'social.backends.facebook.FacebookOAuth2',
        'social.backends.twitter.TwitterOAuth',
        #'social.backends.google.GoogleOAuth2',
        'django.contrib.auth.backends.ModelBackend',
        'account.authentication.EmailAuthBackend',
        

    )

SOCIAL_AUTH_RAISE_EXCEPTIONS = False
SOCIAL_AUTH_FACEBOOK_KEY = '233156223724412' # Facebook App ID
SOCIAL_AUTH_FACEBOOK_SECRET = 'b6a2407cefde906313fe76b94ce5f166' # Facebook App Secret
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']   #Facebook Scope

SOCIAL_AUTH_TWITTER_KEY = 'tweMNNn3gNrEg3UHnuzkWwl5x' # Twitter Consumer Key
SOCIAL_AUTH_TWITTER_SECRET = '2NrARhb8JuH7FiPiYCyfaukOpMdHXaLNiVE0Xr8FI75JbOop77' # Twitter Consumer Secret

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY ='767674675436-s3lrmchrhe1nigbqdfv011h88l9pe025.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET ='kkUTaBitRE7xqirZk8Zjronv'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = 'complete/facebook'

PAYPAL_RECEIVER_EMAIL = 'testbusinessnew@myshop.com'
PAYPAL_TEST = True

ABSOLUTE_URL_OVERRIDES = {
    'auth.user': lambda u: reverse_lazy('account:user_detail', args=[u.username])
}

TEMPLATE_DEBUG = False

REDIS_HOST = '192.168.10.10'
REDIS_PORT = 6379
REDIS_DB = 1

REST_FRAMEWORK = {  
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        
    ],
    
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',

    ],
    
}
CART_SESSION_ID = 'cart'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
#SESSION_SAVE_EVERY_REQUEST = True