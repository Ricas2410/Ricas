from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio, name='portfolio'),
    path('<slug:slug>/', views.project_detail, name='project_detail'),
]
