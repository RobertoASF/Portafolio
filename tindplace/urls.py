from django.urls import path
from .views import user_login
from django.contrib import admin


urlpatterns = [
    path("admin/", admin.site.urls),
    path('login/', user_login, name='login'),
    #path('register/', register, name='register'),
]
