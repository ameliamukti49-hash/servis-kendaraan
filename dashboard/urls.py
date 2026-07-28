from django.urls import path
from . import views

app_name = "dashboard"


urlpatterns = [

    # ==========================
    # DASHBOARD UTAMA
    # ==========================

    path(
        "",
        views.dashboard,
        name="dashboard"
    ),


    # ==========================
    # DASHBOARD ROLE
    # ==========================

    path(
        "admin/",
        views.admin_dashboard,
        name="admin_dashboard"
    ),

    path(
        "service/",
        views.service_dashboard,
        name="service_dashboard"
    ),

    path(
        "mekanik/",
        views.mekanik_dashboard,
        name="mekanik_dashboard"
    ),

    path(
        "kasir/",
        views.kasir_dashboard,
        name="kasir_dashboard"
    ),

    path(
        "pelanggan/",
        views.pelanggan_dashboard,
        name="pelanggan_dashboard"
    ),



    # ==========================
    # MANAJEMEN USER ADMIN
    # ==========================

    path(
        "users/",
        views.user_list,
        name="user_list"
    ),

    path(
        "users/delete/<int:id>/",
        views.user_delete,
        name="user_delete"
    ),
    
    path(
        "users/add/",
        views.user_create,
        name="user_create"
    ),
    
    path(
        "users/edit/<int:id>/",
        views.user_edit,
        name="user_edit"
    ),
    
    path(
        "laporan/",
        views.laporan,
        name="laporan"
    ),
    
    path(
        "grafik/",
        views.grafik,
        name="grafik"
    ),
    
    path(
        "laporan/pdf/",
        views.cetak_pdf,
        name="cetak_pdf"
    ),

]