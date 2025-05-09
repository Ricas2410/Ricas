from django.urls import path
from . import views

urlpatterns = [
    path('', views.development_services, name='development_services'),
    path('<slug:slug>/', views.development_service_detail, name='development_service_detail'),
]
