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
        'kendaraan/<int:pk>/edit/',
        views.kendaraan_update,
        name='kendaraan_update'
    ),

    path(
        'kendaraan/<int:pk>/hapus/',
        views.kendaraan_delete,
        name='kendaraan_delete'
    ),

    # ==========================
    # BOOKING SERVIS
    # ==========================

    path(
        'booking/',
        views.booking_list,
        name='booking_list'
    ),

    path(
        'booking/tambah/',
        views.booking_create,
        name='booking_create'
    ),

    path(
        'booking/<int:pk>/',
        views.booking_detail,
        name='booking_detail'
    ),

    path(
        'booking/<int:pk>/edit/',
        views.booking_update,
        name='booking_update'
    ),

    path(
        'booking/<int:pk>/hapus/',
        views.booking_delete,
        name='booking_delete'
    ),
]