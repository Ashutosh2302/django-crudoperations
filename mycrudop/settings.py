"""
Django settings for mycrudop project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
import environ
env = environ.Env()
environ.Env.read_env()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECURITY_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['django-crudoperations.herokuapp.com', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'crudApp.apps.CrudappConfig',
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

ROOT_URLCONF = 'mycrudop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'mycrudop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'd7saq9oru7urvv',
#         'HOST': 'ec2-34-228-100-83.compute-1.amazonaws.com',
#         'PORT': 5432,
#         'USER': 'wxgabmmhgqvjoy',
#         'PASSWORD': 'c0e68d7d8a6f524fb27b130b1a87f0ac6db4c6d3c57879576752b5144e9dd687',
#
#     }
# }

DATABASES = {
"default": {
    "ENGINE": "djongo",
    "CLIENT": {
        "host": f"mongodb+srv://{env('DB_USERNAME')}:{env('DB_PASSWORD')}@democluster.87rye.mongodb.net/test",
        "username": env('DB_USERNAME'),
        "password": env('DB_PASSWORD'),
        "name": "demodatabase",
    },
}}
# DATABASES = {
#     'default': {
#         'ENGINE': 'djongo',
#         'NAME': 'demodatabase',
#         'CLIENT': {
#           'host': "mongodb+srv://demo:demo@democluster.87rye.mongodb.net/test",
#           'authMechanism': 'SCRAM-SHA-1'
#         }
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators
# postgres://tqvedukxeaiaav:424929ef22c29686387358400524ffef8f00f0e7e5e1111d9f89c221e524e824@ec2-54-157-100-65.compute-1.amazonaws.com:5432/dahdf1k6b6b4p3
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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media_cdn")
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
