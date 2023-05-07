
from django.contrib import admin
from django.urls import path
from . import views
from django.urls import include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('login.urls')),
    path("", include('publicaciones.urls')),
]
