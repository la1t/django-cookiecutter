import locale
import sys
from pathlib import Path

import environ
import sentry_sdk
from sentry_sdk.integrations.celery import CeleryIntegration
from sentry_sdk.integrations.django import DjangoIntegration

env = environ.Env()

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

# GENERAL
# ------------------------------------------------------------------------------
DEBUG = env.bool("DJANGO_DEBUG", default=True)
SECRET_KEY = env("DJANGO_SECRET_KEY", default="!!! SET SECRET KEY !!!")

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["localhost", "127.0.0.1"])


# DATABASES
# ------------------------------------------------------------------------------
DATABASES = {
    "default": env.db("DATABASE_URL", default="sqlite:////%s/db.sqlite3" % BASE_DIR)
}
DATABASES["default"]["ATOMIC_REQUESTS"] = True


# URLS
# ------------------------------------------------------------------------------
ROOT_URLCONF = "{{ cookiecutter.project_slug }}.urls"
WSGI_APPLICATION = "{{ cookiecutter.project_slug }}.wsgi.application"


# APPS
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # "django.contrib.humanize",  # Handy template tags
    "django.contrib.admin",
]

THIRD_PARTY_APPS = [
    "django_extensions",
{%- if cookiecutter.rest_framework == 'y' %}
    "rest_framework",
    "corsheaders",
{%- endif %}
]

LOCAL_APPS = []

INSTALLED_APPS = THIRD_PARTY_APPS + DJANGO_APPS + LOCAL_APPS


# AUTHENTICATION
# ------------------------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# PASSWORDS
# ------------------------------------------------------------------------------
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# MIDDLEWARE
# ------------------------------------------------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
{%- if cookiecutter.rest_framework == 'y' %}
    "corsheaders.middleware.CorsMiddleware",
{%- endif %}
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.common.BrokenLinkEmailsMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# STATIC
# ------------------------------------------------------------------------------
STATIC_ROOT = str(BASE_DIR / "static")
STATIC_URL = "/static/"
STATICFILES_DIRS = []

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# MEDIA
# ------------------------------------------------------------------------------
MEDIA_ROOT = str(BASE_DIR / "uploads")
MEDIA_URL = "/uploads/"


# TEMPLATES
# ------------------------------------------------------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [str(BASE_DIR / "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    }
]


# SECURITY
# ------------------------------------------------------------------------------
if not DEBUG:
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True


{%- if cookiecutter.rest_framework == 'y' %}
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
    "cache-control",
]
{%- endif %}

# EMAIL
# ------------------------------------------------------------------------------
if env("MAILGUN_API_KEY", default=None):
    ANYMAIL = {
        "MAILGUN_API_KEY": env("MAILGUN_API_KEY"),
        "MAILGUN_SENDER_DOMAIN": env("MAILGUN_SENDER_DOMAIN"),
    }
    EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"

DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL", default="webmaster@localhost")
SERVER_EMAIL = env("SERVER_EMAIL", default="root@localhost")


# CELERY
# ------------------------------------------------------------------------------
if USE_TZ:
    CELERY_TIMEZONE = TIME_ZONE
CELERY_BROKER_URL = env("CELERY_BROKER_URL")
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TASK_TIME_LIMIT = 5 * 60
CELERY_TASK_SOFT_TIME_LIMIT = 60


# SENTRY
# ------------------------------------------------------------------------------
SENTRY_DJANGO = env("SENTRY_DJANGO", default=None)
if SENTRY_DJANGO is not None:
    sentry_sdk.init(dsn=SENTRY_DJANGO, integrations=[DjangoIntegration()])

SENTRY_CELERY = env("SENTRY_CELERY", default=None)
if SENTRY_CELERY is not None:
    sentry_sdk.init(SENTRY_CELERY, integrations=[CeleryIntegration()])


# STORAGES
# ------------------------------------------------------------------------------
AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID", default=None)
if AWS_ACCESS_KEY_ID:
    AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY")
    AWS_S3_BUCKET_NAME = env("AWS_S3_BUCKET_NAME")
    AWS_S3_BUCKET_AUTH = False
    AWS_S3_MAX_AGE_SECONDS = 60 * 60 * 24 * 7
    AWS_REGION = env("AWS_S3_REGION_NAME")
    DEFAULT_FILE_STORAGE = "django_s3_storage.storage.S3Storage"


{%- if cookiecutter.rest_framework == 'y' %}
# REST FRAMEWORK
# ------------------------------------------------------------------------------
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
    ],
    "EXCEPTION_HANDLER": "{{ cookiecutter.project_slug }}.core.api.exceptions_handlers.exception_handler",
    "DEFAULT_PERMISSION_CLASSES": [
        "{{ cookiecutter.project_slug }}.core.api.permissions.NotAllowed",
    ],
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
}

SWAGGER_SETTINGS = {
    "DEFAULT_AUTH_SCHEMA_CLASS": "{{ cookiecutter.project_slug }}.core.swagger_inspectors.SwaggerAutoSchema",
    "USER_SESSION_AUTH": False,
    "SECURITY_DEFINITIONS": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
        }
    },
    "PERSIST_AUTH": True,
}
{%- endif %}
