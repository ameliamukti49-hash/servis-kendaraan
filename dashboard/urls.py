# dashboard/urls.py
from django.urls import path
from .views import DashboardRoutingView, user_list_view, user_create_view, user_delete_view[cite: 1]

app_name = 'dashboard'

urlpatterns = [
    # Gateway tunggal untuk mendistribusikan view secara dinamis berdasarkan role user[cite: 1]
    path('', DashboardRoutingView.as_view(), name='index'),[cite: 1]
    
    # Rute Baru: Manajemen User Modul Terintegrasi
    path('users/', user_list_view, name='user_list'),
    path('users/create/', user_create_view, name='user_create'),
    path('users/delete/<int:user_id>/', user_delete_view, name='user_delete'),
    path('grafik/', views.grafik_view, name='grafik_statistik'),
    path('laporan/', views.laporan_view, name='laporan_terpadu'),
    path('invoice/<str:invoice_id>/pdf/', views.export_invoice_pdf, name='export_invoice_pdf'),
]