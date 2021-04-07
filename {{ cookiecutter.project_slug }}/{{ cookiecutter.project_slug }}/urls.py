from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path{% if cookiecutter.rest_framework == 'y' }, include{% endif %}

urlpatterns = [
    path("admin/", admin.site.urls),
{%- if cookiecutter.rest_framework == 'y' %}
    path("api/schema/", include("{{ cookiecutter.project_slug }}.schema.urls")),
{%- endif %}
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
