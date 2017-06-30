# -*- coding: utf-8 -*-
"""
Production Configurations

- Use Amazon's S3 for storing static files and uploaded media
- Use mailgun to send emails
- Use Redis for cache

- Use sentry for error logging


- Use opbeat for error reporting

"""
from __future__ import absolute_import, unicode_literals

from boto.s3.connection import OrdinaryCallingFormat
from django.utils import six

import logging
import os

from .base import *  # noqa

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, os.pardir))

# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Raises ImproperlyConfigured exception if DJANGO_SECRET_KEY not in os.environ
SECRET_KEY = env('DJANGO_SECRET_KEY')


# This ensures that Django will be able to detect a secure connection
# properly on Heroku.
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# raven sentry client
# See https://docs.sentry.io/clients/python/integrations/django/
INSTALLED_APPS += ['raven.contrib.django.raven_compat', ]
RAVEN_MIDDLEWARE = ['raven.contrib.django.raven_compat.middleware.SentryResponseErrorIdMiddleware']
MIDDLEWARE = RAVEN_MIDDLEWARE + MIDDLEWARE
# opbeat integration
# See https://opbeat.com/languages/django/
INSTALLED_APPS += ['opbeat.contrib.django', ]
OPBEAT = {
    'ORGANIZATION_ID': env('DJANGO_OPBEAT_ORGANIZATION_ID'),
    'APP_ID': env('DJANGO_OPBEAT_APP_ID'),
    'SECRET_TOKEN': env('DJANGO_OPBEAT_SECRET_TOKEN')
}
MIDDLEWARE = ['opbeat.contrib.django.middleware.OpbeatAPMMiddleware', ] + MIDDLEWARE


# SECURITY CONFIGURATION
# ------------------------------------------------------------------------------
# See https://docs.djangoproject.com/en/dev/ref/middleware/#module-django.middleware.security
# and https://docs.djangoproject.com/en/dev/howto/deployment/checklist/#run-manage-py-check-deploy

# set this to 60 seconds and then to 518400 when you can prove it works
SECURE_HSTS_SECONDS = 60
SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool(
    'DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS', default=True)
SECURE_CONTENT_TYPE_NOSNIFF = env.bool(
    'DJANGO_SECURE_CONTENT_TYPE_NOSNIFF', default=True)
SECURE_BROWSER_XSS_FILTER = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
CSRF_USE_SESSIONS = True
CSRF_COOKIE_SECURE = True
USE_X_FORWARDED_HOST = True
SECURE_SSL_REDIRECT = env.bool('DJANGO_SECURE_SSL_REDIRECT', default=True)
X_FRAME_OPTIONS = 'ALLOWALL' # <---------- CHANGE THIS !!!!!!!

# SITE CONFIGURATION
# ------------------------------------------------------------------------------
# Hosts/domain names that are valid for this site
# See https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=['*'])#default=['xn--c1ac1acci.xn------dddfnxoenlfghchl4bitc.xn--90ais', 'xn--90a0am.xn------dddfnxoenlfghchl4bitc.xn--90ais', 'xn------dddfnxoenlfghchl4bitc.xn--90ais', '37.143.8.19', 'hosted-by.ihc.ru'])
# END SITE CONFIGURATION

INSTALLED_APPS += ['gunicorn', ]


STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
MEDIA_URL = '/media/'

'''
# STORAGE CONFIGURATION
# ------------------------------------------------------------------------------
# Uploaded Media Files
# ------------------------
# See: http://django-storages.readthedocs.io/en/latest/index.html
INSTALLED_APPS += ['storages', ]

AWS_ACCESS_KEY_ID = env('DJANGO_AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('DJANGO_AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = env('DJANGO_AWS_STORAGE_BUCKET_NAME')
AWS_AUTO_CREATE_BUCKET = True
AWS_QUERYSTRING_AUTH = False
AWS_S3_CALLING_FORMAT = OrdinaryCallingFormat()

# AWS cache settings, don't change unless you know what you're doing:
AWS_EXPIRY = 60 * 60 * 24 * 7

# TODO See: https://github.com/jschneier/django-storages/issues/47
# Revert the following and use str after the above-mentioned bug is fixed in
# either django-storage-redux or boto
AWS_HEADERS = {
    'Cache-Control': six.b('max-age=%d, s-maxage=%d, must-revalidate' % (
        AWS_EXPIRY, AWS_EXPIRY))
}

# URL that handles the media served from MEDIA_ROOT, used for managing
# stored files.

#  See:http://stackoverflow.com/questions/10390244/
from storages.backends.s3boto import S3BotoStorage
StaticRootS3BotoStorage = lambda: S3BotoStorage(location='static')
MediaRootS3BotoStorage = lambda: S3BotoStorage(location='media')
DEFAULT_FILE_STORAGE = 'config.settings.production.MediaRootS3BotoStorage'

MEDIA_URL = 'https://s3.amazonaws.com/%s/media/' % AWS_STORAGE_BUCKET_NAME

# Static Assets
# ------------------------

STATIC_URL = 'https://s3.amazonaws.com/%s/static/' % AWS_STORAGE_BUCKET_NAME
STATICFILES_STORAGE = 'config.settings.production.StaticRootS3BotoStorage'
# See: https://github.com/antonagestam/collectfast
# For Django 1.7+, 'collectfast' should come before
# 'django.contrib.staticfiles'
AWS_PRELOAD_METADATA = True
'''

INSTALLED_APPS = ['collectfast', ] + INSTALLED_APPS
# COMPRESSOR
# ------------------------------------------------------------------------------
COMPRESSOR_STORAGE = 'compressor.storage.CompressorFileStorage'
COMPRESS_URL = STATIC_URL
COMPRESS_ENABLED = env.bool('COMPRESS_ENABLED', default=True)
COMPRESS_OFFLINE = env.bool('COMPRESS_OFFLINE', default=True)
#COMPRESS_JS_FILTERS = ['compressor.filters.closure.ClosureCompilerFilter']
#COMPRESS_CLOSURE_COMPILER_BINARY = '/usr/share/java/closure-compiler.jar'
#COMPRESS_JS_FILTERS = ['compressor.filters.jsmin.SlimItFilter']
#COMPRESS_JS_FILTERS = ['compressor.filters.jsmin.JSMinFilter']
#COMPRESS_CSS_FILTERS = ['compressor.filters.cleancss.CleanCSSFilter']
#COMPRESS_PARSER = 'compressor.parser.LxmlParser'
# EMAIL
# ------------------------------------------------------------------------------
DEFAULT_FROM_EMAIL = env('DJANGO_DEFAULT_FROM_EMAIL',
                         default='gglobal <noreply@xn------dddfnxoenlfghchl4bitc.xn--90ais>')
EMAIL_SUBJECT_PREFIX = env('DJANGO_EMAIL_SUBJECT_PREFIX', default='[gglobal]')
SERVER_EMAIL = env('DJANGO_SERVER_EMAIL', default=DEFAULT_FROM_EMAIL)

# Anymail with Mailgun
INSTALLED_APPS += ['anymail', ]
ANYMAIL = {
    'MAILGUN_API_KEY': env('DJANGO_MAILGUN_API_KEY'),
    'MAILGUN_SENDER_DOMAIN': env('MAILGUN_SENDER_DOMAIN')
}
EMAIL_BACKEND = 'anymail.backends.mailgun.MailgunBackend'

# TEMPLATE CONFIGURATION
# ------------------------------------------------------------------------------
# See:
# https://docs.djangoproject.com/en/dev/ref/templates/api/#django.template.loaders.cached.Loader
TEMPLATES[0]['OPTIONS']['loaders'] = [
    ('django.template.loaders.cached.Loader', [
        'django.template.loaders.filesystem.Loader', 'django.template.loaders.app_directories.Loader', ]),
]

# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# Uses Amazon RDS for database hosting, which doesn't follow the Heroku-style spec
DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': env('RDS_DB_NAME'),
        'USER': env('RDS_USERNAME'),
        'PASSWORD': env('RDS_PASSWORD'),
        'HOST': env('RDS_HOSTNAME'),
        'PORT': env('RDS_PORT'),
        'CONN_MAX_AGE': 600,
    }
}
#DATABASES['default'] = env.db('DATABASE_URL')


# CACHING
# ------------------------------------------------------------------------------
#REDIS_LOCATION = 'redis://{}:{}/0'.format(
#    env('REDIS_ENDPOINT_ADDRESS'),
#    env('REDIS_PORT')
#)

REDIS_LOCATION = '/tmp/redis.sock'

# Heroku URL does not pass the DB number, so we parse it in
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': REDIS_LOCATION,
        'OPTIONS': {
            #'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            "CLIENT_CLASS": "django_redis.client.HerdClient",
            "PICKLE_VERSION": -1,
            #"COMPRESSOR": "django_redis.compressors.zlib.ZlibCompressor",
            "COMPRESSOR": "django_redis.compressors.lzma.LzmaCompressor",
            "PARSER_CLASS": "redis.connection.HiredisParser",
            "CONNECTION_POOL_KWARGS": {"max_connections": 100},
            "SOCKET_CONNECT_TIMEOUT": 5,  # in seconds
            "SOCKET_TIMEOUT": 5,  # in seconds
            'IGNORE_EXCEPTIONS': True,  # mimics memcache behavior.
                                        # http://niwinz.github.io/django-redis/latest/#_memcached_exceptions_behavior
        }
    }
}

SESSION_SERIALIZER='django.contrib.sessions.serializers.PickleSerializer'
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
#SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"
#DJANGO_REDIS_LOG_IGNORED_EXCEPTIONS = True



# Sentry Configuration
SENTRY_DSN = env('DJANGO_SENTRY_DSN', default='https://56bb387ee6ef4e7bb513862157edac13:516039c011914079a7b3c4d36bd6fe2b@sentry.io/158504')
SENTRY_CLIENT = env('DJANGO_SENTRY_CLIENT', default='raven.contrib.django.raven_compat.DjangoClient')
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry', ],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
                      '%(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console', ],
            'propagate': False,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console', ],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console', ],
            'propagate': False,
        },
        'django.security.DisallowedHost': {
            'level': 'ERROR',
            'handlers': ['console', 'sentry', ],
            'propagate': False,
        },
        'nplusone': {
            'level': 'WARN',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}
SENTRY_CELERY_LOGLEVEL = env.int('DJANGO_SENTRY_LOG_LEVEL', logging.INFO)
RAVEN_CONFIG = {
    'CELERY_LOGLEVEL': env.int('DJANGO_SENTRY_LOG_LEVEL', logging.INFO),
    'DSN': SENTRY_DSN
}

# Custom Admin URL, use {% url 'admin:index' %}
ADMIN_URL = env('DJANGO_ADMIN_URL')

# Your production stuff: Below this line define 3rd party library settings
# ------------------------------------------------------------------------------




# CELERY SETTINGS
# ------------------------------------------------------------------------------
#CELERY_QUEUES = (
#   Queue('high', Exchange('high'), routing_key='high'),
#    Queue('normal', Exchange('normal'), routing_key='normal'),
#    Queue('low', Exchange('low'), routing_key='low'),
#)
#import djcelery

CELERY_DEFAULT_QUEUE = 'normal'
CELERY_DEFAULT_EXCHANGE = 'normal'
CELERY_DEFAULT_ROUTING_KEY = 'normal'

CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
CELERY_SEND_TASK_ERROR_EMAILS = True
BROKER_URL = REDIS_LOCATION
CELERY_RESULT_BACKEND = REDIS_LOCATION
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Europe/Minsk'
#djcelery.setup_loader()

