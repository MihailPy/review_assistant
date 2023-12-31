"""
Django settings for review_assistant project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'review_assistant/static/'),
]

STATIC_ROOT = BASE_DIR / 'static'
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-osb3v70gwf%gscgz6&*%e5e!sn6503nx50pime)g&*r%&z5!3%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

if DEBUG:
    CSRF_TRUSTED_ORIGINS = ['http://392f-178-176-214-192.ngrok-free.app', 'https://392f-178-176-214-192.ngrok-free.app']
CORS_ORIGIN_WHITELIST = ['392f-178-176-214-192.ngrok-free.app']
ALLOWED_HOSTS = ['392f-178-176-214-192.ngrok-free.app', '127.0.0.1:8000', '127.0.0.1',]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace('\\', '/')
MEDIA_URL = '/media/'

# Application definition

INSTALLED_APPS = [
    'customers',
    'executors',
    'orders',
    'tasks',
    'home',
    'webpush',
    'review_assistant',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'review_assistant.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'review_assistant/templates')
        ],
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

LOGIN_REDIRECT_URL = '/home_page/'

WSGI_APPLICATION = 'review_assistant.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'review_assistant',
        'USER': 'postgres',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
WEBPUSH_SETTINGS = {
   "VAPID_PUBLIC_KEY": "BGQewwx1M6bXefiiKzaNvLdr1KOKry4Vvdg5f0Rv8KhU4B0nuq3TpgLwqmzHU4-5uyNPXdU_NTZcpoKMsGnrVBo",
   "VAPID_PRIVATE_KEY": "rFTAqbdCeIreR8CLgC1Ruqb2sQg2GaTelkI82axfUEw",
   "VAPID_ADMIN_EMAIL": "mihailpy02@gmail.com"
}
NOTIFICATION_KEY = "BBFpaAyv2HN7jg2bJeWXrIne3HpkXdscsS0QWR5wH1bSIX4YpjDtYX36OmWBQV-dv09bnaG2uey74Fx_FuTNVdA"
# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
