from django.urls import path
from . import views

app_name = 'mekanik'

urlpatterns = [
    path('', views.dashboard_mekanik, name='dashboard'),
    path('data/', views.data_mekanik, name='data_mekanik'),
    path('tambah/', views.tambah_mekanik, name='tambah_mekanik'),
    path('workorder/', views.daftar_workorder, name='daftar_workorder'),
    path('workorder/tambah/', views.tambah_workorder, name='tambah_workorder'),
    path('workorder/<int:pk>/',views.detail_servis,name='detail_servis'),
]