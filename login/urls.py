from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('todos-productos/', views.all_products, name='all_products'),
    path('enviar_correo/', views.enviar_correo, name='enviar_correo'),
    path('weather/', views.weather, name='weather'),
    path('product_detail/<str:prod_id>/', views.product_detail, name='product_detail'),
]

