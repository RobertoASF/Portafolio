from django.urls import path
from . import views

urlpatterns = [
    # ... otras URL de tu aplicación
    path('login/', views.login, name='login'),
]
