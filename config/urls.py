from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

# DRF + Swagger imports
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Swagger schema setup
schema_view = get_schema_view(
    openapi.Info(
        title="Poll API",
        default_version='v1',
        description="Backend API for Online Poll System",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),                          # Admin panel
    path('api/', include('polls.urls')),                      # Poll API endpoints
    path('', RedirectView.as_view(url='/api/', permanent=False)),  # Redirect root to /api/
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Swagger docs
]
