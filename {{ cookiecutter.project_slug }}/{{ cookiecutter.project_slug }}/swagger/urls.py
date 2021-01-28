from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

app_name = "swagger"

schema_view = get_schema_view(
    public=True,
    info=openapi.Info(
        title="{{ cookiecutter.project_name }} API",
        default_version="v1",
        description="API Doc для {{ cookiecutter.project_name }}",
    ),
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("", schema_view.with_ui("swagger", cache_timeout=0), name="schema"),
]
