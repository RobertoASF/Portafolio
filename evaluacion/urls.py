from django.urls import path
from . import views

urlpatterns = [
    path('evaluation/', views.evaluation, name='evaluation'),
    path('evaluation_done/', views.evaluation_done, name='evaluation_done'),
]
