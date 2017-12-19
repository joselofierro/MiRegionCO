"""
Django settings for MiRegionCO project.

Generated by 'django-admin startproject' using Django 1.11.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from django.urls import reverse_lazy

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9v2rrct&d)!7-b97u7md2u7cb7!cb%%k^ls+1s1s7mxt4k6m4r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [

    '.elasticbeanstalk.com',
    '54.165.204.105',
    '34.231.1.194',
    '192.168.10.245',
    '127.0.0.1',
    'miregion.co',
    'www.miregion.co'
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.usuario',
    'apps.categoria',
    'apps.imagen',
    'apps.noticia',
    'apps.tag',
    'apps.sitio',
    'apps.categoria_mapa',
    'apps.subcategoria_mapa',
    'apps.grupo',
    'apps.prueba_tag',
    'apps.estadistica',
    'apps.ventas.categoria_producto',
    'apps.ventas.cliente',
    'apps.ventas.cotizacion',
    'apps.ventas.detalle',
    'apps.ventas.producto',
    'apps.ventas.subcategoria_producto',
    'apps.ventas.vendedor',
    'apps.notificaciones',
    'apps.activacion_youtuber',
    'apps.web',
    'rest_framework',
    'storages',
    'fcm_django',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'MiRegionCO.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'MiRegionCO.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

if 'RDS_DB_NAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': 'JoseFierro_2017',
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'miregionco',
            'USER': 'postgres',
            'PASSWORD': 'backend17',
            'HOST': 'localhost',
            'PORT': 5432,
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

LANGUAGE_CODE = 'es-co'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = True

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'jfierro985@gmail.com'
EMAIL_HOST_PASSWORD = 'eugenio985'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "..", "www", "static")
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

# MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "..", "www", "media")

AWS_STORAGE_BUCKET_NAME = 'miregionco'
AWS_ACCESS_KEY_ID = 'AKIAIKEWELJW4WU47OUQ'
AWS_SECRET_ACCESS_KEY = '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'

# Tell django-storages that when coming up with the URL for an item in S3 storage, keep
# it simple - just use this domain plus the path. (If this isn't set, things get complicated).
# This controls how the `static` template tag from `staticfiles` gets expanded, if you're using it.
# We also use it in the next setting.
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

# This is used by the `static` template tag from `static`, if you're using that. Or if anything else
# refers directly to STATIC_URL. So it's safest to always set it.
# STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN

# Tell the staticfiles app to use S3Boto storage when writing the collected static files (when
# you run `collectstatic`).
# STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)

MEDIAFILES_LOCATION = 'media'
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'

# SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = 3600
# SESSION_SAVE_EVERY_REQUEST = True

# (Firebase Cloud Messaging)
FCM_DJANGO_SETTINGS = {

    "FCM_SERVER_KEY": "AAAAMa4kYOQ:APA91bG7VC1VzvvNAOnID38pC9LRivih0jqCa2KLM6cf0L5CiFE5aOa5h7f2c7sA-gCoRmSVws0XtFr2k5yGBy-Jbn-jtf0HiYmdjzVUQgqY4SASRscEs9HbH3hveczNPT5JOi2Jfu9A",
    # true if you want to have only one active device per registered user at a time
    # default: False
    "ONE_DEVICE_PER_USER": True,
    # devices to which notifications cannot be sent,
    # are deleted upon receiving error response from FCM
    # default: False
    "DELETE_INACTIVE_DEVICES": False,
}

# Cache
CACHE_API_CATEGORIA_MAPA = 'api_categoria_mapa'
CACHE_API_CATEGORIA_NOTICIAS = 'api_categoria_noticias'
CACHE_API_NOTICIAS = 'api_noticias'
CACHE_API_NOTICIAS2 = 'api_noticias2'
CACHE_API_NOTICIASWEB = 'api_noticias_web'
CACHE_API_NOTICIAS_DESTACADAS = 'api_noticias_destacadas'
CACHE_API_NOTICIASXCATEGORIA = 'api_noticiasxcategoria'
CACHE_API_NOTICIASXCATEGORIA2 = 'api_noticiasxcategoria2'
CACHE_API_NOTICIAS_DESTACADAS_CATEGORIA = 'api_noticias_destacadas_categoria'
CACHE_API_SITIOS = 'api_sitios'
CACHE_API_SITIOSXSUBCATEGORIA = 'api_sitiosxsubcategoria'
CACHE_API_PORTAFOLIO = 'api_portafolio'
CACHE_API_COTIZACIONES = 'api_cotizaciones'
CACHE_API_USUARIOS = 'api_usuarios'
CACHES = {

    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache/default',
        'TIMEOUT': None
    },

    CACHE_API_CATEGORIA_MAPA: {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache/api/categoria_mapa',
        'TIMEOUT': None

    },
    CACHE_API_NOTICIAS: {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache/api/noticias',
        'TIMEOUT': None

    },

    CACHE_API_NOTICIAS2: {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache/api/noticias2',
        'TIMEOUT': None

    },

    CACHE_API_NOTICIASWEB: {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache/api/noticias_web',
        'TIMEOUT': None

    },

    CACHE_API_NOTICIAS_DESTACADAS: {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache/api/noticias_destacadas',
        'TIMEOUT': None

    },
    CACHE_API_NOTICIASXCATEGORIA: {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache/api/noticiasxcategoria',
        'TIMEOUT': None
    },
    CACHE_API_NOTICIASXCATEGORIA2: {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache/api/noticiasxcategoria2',
        'TIMEOUT': None
    },
    CACHE_API_CATEGORIA_NOTICIAS: {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache/api/categoria_noticias',
        'TIMEOUT': None

    },

    CACHE_API_SITIOS: {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache/api/sitios',
        'TIMEOUT': None

    },

    CACHE_API_SITIOSXSUBCATEGORIA: {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache/api/sitiosxsubcategoria',
        'TIMEOUT': None

    },

    CACHE_API_PORTAFOLIO: {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache/api/portafolio',
        'TIMEOUT': None

    },
    CACHE_API_COTIZACIONES: {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache/api/cotizaciones',
        'TIMEOUT': None

    },
    CACHE_API_USUARIOS: {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache/api/usuarios',
        'TIMEOUT': None

    },
    CACHE_API_NOTICIAS_DESTACADAS_CATEGORIA: {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache/api/noticias_destacadas_categoria',
        'TIMEOUT': None
    }

}

LOGIN_URL = reverse_lazy('user:index')
