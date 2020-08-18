from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
{% if cookiecutter.custom_404_page == 'y' -%}
from {{ cookiecutter.project_slug }}.main.views import handler404
{%- endif %}

urlpatterns = [
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    {% if cookiecutter.custom_404_page == 'y' -%}
    urlpatterns.append(path('404/', handler404))
    {%- endif %}

{% if cookiecutter.custom_404_page == 'y' -%}
handler404 = '{{ cookiecutter.project_slug }}.main.views.handler404'
{%- endif %}
