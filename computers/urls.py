from django.urls import path
from . import views

urlpatterns = [
    path('', views.computer_categories, name='computer_categories'),
    path('ecommerce/', views.redirect_to_ecommerce, name='redirect_to_ecommerce'),
    path('network/', views.network_services, name='network_services'),
    path('network/<slug:slug>/', views.network_service_detail, name='network_service_detail'),
    path('<slug:slug>/', views.computer_category_detail, name='computer_category_detail'),
    path('<slug:category_slug>/<slug:product_slug>/', views.computer_product_detail, name='computer_product_detail'),
]
