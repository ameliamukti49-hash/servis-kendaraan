from django.urls import path
from . import views


urlpatterns = [


    path(
        'sparepart/',
        views.daftar_sparepart,
        name='daftar_sparepart'
    ),


    path(
        'sparepart/tambah/',
        views.tambah_sparepart,
        name='tambah_sparepart'
    ),


    path(
        'sparepart/edit/<int:pk>/',
        views.edit_sparepart,
        name='edit_sparepart'
    ),


    path(
        'sparepart/hapus/<int:pk>/',
        views.hapus_sparepart,
        name='hapus_sparepart'
    ),



    path(
        'jasa/',
        views.daftar_jasa,
        name='daftar_jasa'
    ),


    path(
        'jasa/tambah/',
        views.tambah_jasa,
        name='tambah_jasa'
    ),


    path(
        'jasa/edit/<int:pk>/',
        views.edit_jasa,
        name='edit_jasa'
    ),


    path(
        'jasa/hapus/<int:pk>/',
        views.hapus_jasa,
        name='hapus_jasa'
    ),



    # PEMBAYARAN

    path(
        'pembayaran/',
        views.daftar_pembayaran,
        name='daftar_pembayaran'
    ),


    path(
        'pembayaran/tambah/',
        views.tambah_pembayaran,
        name='tambah_pembayaran'
    ),


    path(
        'pembayaran/<int:pk>/',
        views.detail_pembayaran,
        name='detail_pembayaran'
    ),
    
    path(
        'pembayaran/',
        views.daftar_pembayaran,
        name='daftar_pembayaran'
    ),

    path(
        'pembayaran/tambah/',
        views.tambah_pembayaran,
        name='tambah_pembayaran'
    ),

    path(
        'pembayaran/<int:pk>/',
        views.detail_pembayaran,
        name='detail_pembayaran'
    ),
    
    path(
        'invoice/<int:pk>/',
        views.cetak_invoice,
        name='cetak_invoice'
    ),

]