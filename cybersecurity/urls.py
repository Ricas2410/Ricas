from django.urls import path
from . import views

urlpatterns = [
    path('', views.cybersecurity_services, name='cybersecurity_services'),
    path('<slug:slug>/', views.cybersecurity_service_detail, name='cybersecurity_service_detail'),
]
