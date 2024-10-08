"""onestep URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.conf import settings
from django.conf.urls.static import static
from dotenv import load_dotenv
import os

load_dotenv()

schema_view = get_schema_view(
    openapi.Info(
        title="Django API",
        default_version="v1",
    ),
    public=True,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("api/", include("tickets.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Django admin"
admin.site.site_title = "Django admin"
admin.site.index_title = "Welcome to Django admin panel"

# if settings.DEBUG or os.environ.get('MEDIA_SERVER')=='True':
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
