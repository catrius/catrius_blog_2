"""
URL configuration for catrius_blog_2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from blog.urls import router as blog_router

router = routers.DefaultRouter()
router.registry.extend(blog_router.registry)

paths = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api-auth/', include('rest_framework.urls', namespace = 'rest_framework')),
    path('', include(blog_router.urls)),
]

if settings.DEBUG:
    static_paths = static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    media_paths = static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

    urlpatterns = paths + static_paths + media_paths
else:
    urlpatterns = paths
