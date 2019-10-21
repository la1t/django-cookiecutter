import os

import environ
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

env = environ.Env()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# --------------------------------------------------------------------------------------------------
# - BASE -------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------

SECRET_KEY = env('SECRET_KEY', default='!!! SET SECRET KEY !!!')

DEBUG = env.bool('DEBUG', default=True)

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['localhost', '127.0.0.1'])


DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LOCAL_APPS = [
    {% if cookiecutter.use_custom_user_model == 'y' -%}
    '{{ cookiecutter.project_slug }}.users',
    {%- endif %}
]

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'

# --------------------------------------------------------------------------------------------------
# - DATABASES --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------

DATABASES = {
    'default': env.db('DATABASE_URL', default='sqlite:////%s/db.sqlite3' % BASE_DIR)
}

# --------------------------------------------------------------------------------------------------
# - AUTHENTICATION ---------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------

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

{% if cookiecutter.use_custom_user_model == 'y' %}
AUTH_USER_MODEL = 'users.ExtUser'
{% endif -%}

# -----------------------------------------------------------------------------------------------
# - SECURITY ------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------

if not DEBUG:
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    X_FRAME_OPTIONS = 'DENY'

# --------------------------------------------------------------------------------------------------
# - INTERNATIONALIZATION ---------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------

LANGUAGE_CODE = 'ru-RU'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# --------------------------------------------------------------------------------------------------
# - STATIC FILES -----------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------

STATIC_URL = '/static/'
STATIC_PATH = os.path.join(BASE_DIR, 'static')
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

MEDIA_URL = '/uploads/'
MEDIA_PATH = os.path.join(BASE_DIR, 'uploads')

# --------------------------------------------------------------------------------------------------
# - SENTRY TRACKING --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------

if env('SENTRY_DSN', default=None):
    sentry_sdk.init(
        dsn=env('SENTRY_DSN'),
        integrations=[DjangoIntegration()],
        environment=env('SENTRY_ENV', default='staging')
    )

# --------------------------------------------------------------------------------------------------
# - EMAIL ------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------

if env('MAILGUN_API_KEY', default=None):
    ANYMAIL = {
        'MAILGUN_API_KEY': env('MAILGUN_API_KEY'),
        'MAILGUN_SENDER_DOMAIN': env('MAILGUN_SENDER_DOMAIN'),
    }
    EMAIL_BACKEND = 'anymail.backends.mailgun.EmailBackend'

DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL', default='webmaster@localhost')
SERVER_EMAIL = env('SERVER_EMAIL', default='root@localhost')
