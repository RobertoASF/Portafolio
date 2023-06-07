from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('publicar/', views.create_product, name='create_product'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
