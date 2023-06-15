from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

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
    path('favorites/', views.favorites, name='favorites'),
    path('like_product/<str:product_id>', views.like_product, name='like_product'),
    path('comprar/<str:prod_id>/', views.comprar_producto, name='comprar_producto'),
    path('confirmacion/', views.pagina_de_confirmacion, name='pagina_de_confirmacion'), 
    path('toggle_user_active/', views.toggle_user_active, name='toggle_user_active'),
    path('inactive/', views.inactive, name='inactive'),
    path('toggle_product_active/', views.toggle_product_active, name='toggle_product_active'),
    path('sold_products/', views.sold_products, name='sold_products'),
    path('rate_seller/<str:seller_id>', views.rate_seller, name='rate_seller'),
    path('products-cards/', views.products_cards_view, name='products-cards'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

