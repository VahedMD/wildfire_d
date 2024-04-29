
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/auth/", include('djoser.urls')),
    path("api/v1/auth/", include('djoser.urls.jwt')),
    path("", TemplateView.as_view(template_name='index.html')),
    path("robots.txt/", TemplateView.as_view(template_name="robots.txt",
         content_type="text/plain")),
    path("manifest.json/", TemplateView.as_view(template_name='manifest.json')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
