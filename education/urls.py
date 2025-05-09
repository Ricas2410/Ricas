from django.urls import path
from . import views

urlpatterns = [
    path('', views.education_services, name='education_services'),
    path('<slug:slug>/', views.education_service_detail, name='education_service_detail'),
]
