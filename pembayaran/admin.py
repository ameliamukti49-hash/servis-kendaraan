from django.contrib import admin
from .models import (
    Sparepart,
    JasaServis,
    DetailSparepart,
    DetailJasa,
    Pembayaran,
)


@admin.register(Sparepart)
class SparepartAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama', 'harga', 'stok')
    search_fields = ('nama',)


@admin.register(JasaServis)
class JasaServisAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama', 'biaya')
    search_fields = ('nama',)


@admin.register(DetailSparepart)
class DetailSparepartAdmin(admin.ModelAdmin):
    list_display = ('id', 'workorder', 'sparepart', 'jumlah', 'subtotal')
    list_filter = ('sparepart',)


@admin.register(DetailJasa)
class DetailJasaAdmin(admin.ModelAdmin):
    list_display = ('id', 'workorder', 'jasa', 'subtotal')
    list_filter = ('jasa',)


@admin.register(Pembayaran)
class PembayaranAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'workorder',
        'total_sparepart',
        'total_jasa',
        'total_bayar',
        'metode',
        'status',
        'tanggal_bayar',
    )

    list_filter = ('metode', 'status')
    search_fields = ('workorder__nomor_wo',)