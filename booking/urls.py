from django.urls import path
from . import views

urlpatterns = [

    # ==========================
    # DATA KENDARAAN
    # ==========================

    path(
        'kendaraan/',
        views.kendaraan_list,
        name='kendaraan_list'
    ),

    path(
        'kendaraan/tambah/',
        views.kendaraan_create,
        name='kendaraan_create'
    ),

    path(
        'kendaraan/edit/<int:pk>/',
        views.kendaraan_update,
        name='kendaraan_update'
    ),

    path(
        'kendaraan/hapus/<int:pk>/',
        views.kendaraan_delete,
        name='kendaraan_delete'
    ),

    # ==========================
    # BOOKING SERVIS
    # ==========================

    path(
        '',
        views.booking_list,
        name='booking_list'
    ),

    path(
        'tambah/',
        views.booking_create,
        name='booking_create'
    ),

    path(
        'edit/<int:pk>/',
        views.booking_update,
        name='booking_update'
    ),

    path(
        'hapus/<int:pk>/',
        views.booking_delete,
        name='booking_delete'
    ),

    path(
        'detail/<int:pk>/',
        views.booking_detail,
        name='booking_detail'
    ),

]