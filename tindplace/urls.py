from django.urls import path
from .views import login_view, register
from django.contrib import admin


urlpatterns = [
    path("admin/", admin.site.urls),
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
]
