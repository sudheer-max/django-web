"""
Django settings for intel project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = "suddymax0001@gmail.com"
EMAIL_HOST_PASSWORD = "ben10new"
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6a=3ghrmjd0x@znu_txehr=v(xeb=)vice=71)2=u@giv7_+!l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'intellect.apps.IntellectConfig',
    'contact.apps.ContactConfig',
    'ckeditor',
    'ckeditor_uploader',
    'crispy_forms',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    
]
CKEDITOR_UPLOAD_PATH = "uploads/"
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'intel.urls'

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

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

WSGI_APPLICATION = 'intel.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_root')

CRISPY_TEMPLATE_PACK = 'bootstrap4'




SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_REFERRER_POLICY = None
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_REFERRER_POLICY = 'origin'


SITE_ID = 1

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'

ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_CONFIRM_EMAIL_ON_GET = False
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = LOGIN_URL
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = None

ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3
ACCOUNT_EMAIL_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = None
ACCOUNT_EMAIL_SUBJECT_PREFIX = "My subject:"
ACCOUNT_DEFAULT_HTTP_PROTOCOL = "http"

ACCOUNT_LOGOUT_ON_GET = False
ACCOUNT_LOGOUT_REDIRECT_URL = "/"
ACCOUNT_SIGNUP_FORM_CLASS = None
ACCOUNT_SIGNUP_PASSWORD_VARIFICATION = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USER_MODEL_USERNAME_FIELD = "username"
ACCOUNT_USER_MODEL_EMAIL_FIELD = "email"

ACCOUNT_USERNAME_MIN_LENGTH = 5
ACCOUNT_USERNAME_BLACKLIST = []
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_PASSWORD_INPUT_RENDER_VALUE = False
ACCOUNT_PASSWORD_MIN_LENGTH = 6
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True