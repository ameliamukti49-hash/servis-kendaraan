from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    # Dashboard Utama & Grafik
    path('', views.dashboard_home, name='home'),
    
    # Manajemen User (CRUD)
    path('users/', views.user_list, name='user_list'),
    path('users/add/', views.user_create, name='user_create'),
    path('users/edit/', views.user_update, name='user_update'),
    path('users/delete/<int:pk>/', views.user_delete, name='user_delete'),
    
    # Laporan
    path('laporan/booking/', views.laporan_booking, name='laporan_booking'),
    path('laporan/servis/', views.laporan_servis, name='laporan_servis'),
    path('laporan/pembayaran/', views.laporan_pembayaran, name='laporan_pembayaran'),
    
    # Trigger Cetak PDF
    path('laporan/booking/pdf/', views.cetak_booking_pdf, name='cetak_booking_pdf'),
    path('laporan/servis/pdf/', views.cetak_servis_pdf, name='cetak_servis_pdf'),
    path('laporan/pembayaran/pdf/', views.cetak_pembayaran_pdf, name='cetak_pembayaran_pdf'),
]