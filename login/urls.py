from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('enviar_correo/', views.enviar_correo, name='enviar_correo'),
]
