from django.urls import path
from . import views

urlpatterns = [
    path('publicar/', views.create_product, name='create_product'),
]
