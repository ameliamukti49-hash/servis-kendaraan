from django.urls import path
from . import views

urlpatterns = [
    # ==========================
    # Sparepart
    # ==========================
    path('sparepart/', views.daftar_sparepart, name='daftar_sparepart'),
    path('sparepart/tambah/', views.tambah_sparepart, name='tambah_sparepart'),
    path('sparepart/edit/<int:pk>/', views.edit_sparepart, name='edit_sparepart'),
    path('sparepart/hapus/<int:pk>/', views.hapus_sparepart, name='hapus_sparepart'),

    # ==========================
    # Jasa Servis
    # ==========================
    path('jasa/', views.daftar_jasa, name='daftar_jasa'),
    path('jasa/tambah/', views.tambah_jasa, name='tambah_jasa'),
    path('jasa/edit/<int:pk>/', views.edit_jasa, name='edit_jasa'),
    path('jasa/hapus/<int:pk>/', views.hapus_jasa, name='hapus_jasa'),

    # ==========================
    # Detail Sparepart
    # ==========================
    path(
        'workorder/<int:workorder_id>/sparepart/',
        views.daftar_detail_sparepart,
        name='daftar_detail_sparepart'
    ),
    path(
        'workorder/<int:workorder_id>/sparepart/tambah/',
        views.tambah_detail_sparepart,
        name='tambah_detail_sparepart'
    ),

    # ==========================
    # Detail Jasa
    # ==========================
    path(
        'workorder/<int:workorder_id>/jasa/',
        views.daftar_detail_jasa,
        name='daftar_detail_jasa'
    ),
    path(
        'workorder/<int:workorder_id>/jasa/tambah/',
        views.tambah_detail_jasa,
        name='tambah_detail_jasa'
    ),

    # ==========================
    # Pembayaran
    # ==========================
    path('pembayaran/', views.daftar_pembayaran, name='daftar_pembayaran'),
    path('pembayaran/tambah/<int:workorder_id>/', views.tambah_pembayaran, name='tambah_pembayaran'),
    path('pembayaran/edit/<int:pk>/', views.edit_pembayaran, name='edit_pembayaran'),
    path('pembayaran/hapus/<int:pk>/', views.hapus_pembayaran, name='hapus_pembayaran'),

    # ==========================
    # Invoice
    # ==========================
    path('invoice/<int:pk>/', views.invoice, name='invoice'),
]