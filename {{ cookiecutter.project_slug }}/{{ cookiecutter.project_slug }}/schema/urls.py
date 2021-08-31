from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.urls import path

app_name = "docs"

urlpatterns = [
    path("", SpectacularSwaggerView.as_view(url_name="docs:schema"), name="swagger-ui"),
    path("swagger.json", SpectacularAPIView.as_view(), name="schema"),
]
