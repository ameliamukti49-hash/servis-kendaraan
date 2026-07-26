from django.urls import path
from . import views

urlpatterns = [
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('pelanggan-dashboard/', views.pelanggan_dashboard, name='pelanggan_dashboard'),
    path('mekanik-dashboard/', views.mekanik_dashboard, name='mekanik_dashboard'),
    path('kasir-dashboard/', views.kasir_dashboard, name='kasir_dashboard'),
]