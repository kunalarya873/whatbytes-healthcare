from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# __define-ocg__ Swagger schema definition
schema_view = get_schema_view(
   openapi.Info(
      title="Healthcare Backend API",
      default_version='v1',
      description="API documentation for managing users, patients, doctors, and their mappings.",
      terms_of_service="https://www.example.com/terms/",
      contact=openapi.Contact(email="support@example.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.urls')),
    path('api/patients/', include('patients.urls')),
    path('api/doctors/', include('doctors.urls')),
    path('api/mappings/', include('mappings.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)