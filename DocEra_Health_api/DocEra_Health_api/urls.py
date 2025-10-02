from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from core.views import ApiRootView
from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [
    # Django admin (Custom Jazzmin-themed) for staff/doctors.
    path('admin/', admin.site.urls),

    # API Root View at project root
    path('', ApiRootView.as_view(), name='api-root'),

    # Djoser Authentication Endpoints
    re_path(r'^auth/', include('djoser.urls')), # Djoser user endpoints: /auth/users/, activation, etc.
    re_path(r'^auth/', include('djoser.urls.jwt')), # JWT: /auth/jwt/create/ for login.


    # Browsable API Authentication
    path('api-auth/', include('rest_framework.urls')),  # Login/logout for browsable API

    # API Versioning: Nest all app endpoints under /api/v1/
    path('api/v1/', include([
        path('appointment/', include('appointment.urls')), # Online and Offline Appointments, payments, webhooks, cancel Appointment.
        path('contact_us/', include('contact_us.urls')), # Contact Us CRUD endpoints.
        path('doctor/', include('doctor.urls')), # Doctors, designations, specializations, times, reviews endpoints.
        path('patient/', include('patient.urls')), # Patient profiles endpoints.
        path('service/', include('service.urls')), # Medical services CRUD endpoints.
    ])),
    
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'), # OpenAPI schema download.
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='schema-swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='schema-redoc'),

    # ckeditor-5 upload path
    path('ckeditor5/upload/', include('django_ckeditor_5.urls'), name='ck_editor_5_upload_file'),
    # CKEditor file uploads for rich text fields (e.g., doctor bio, service description).
]

# Add Debug Toolbar URLs (only active in DEBUG=True)
urlpatterns += debug_toolbar_urls()

# Serve media files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
